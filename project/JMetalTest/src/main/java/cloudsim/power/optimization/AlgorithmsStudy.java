package cloudsim.power.optimization;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.uma.jmetal.algorithm.Algorithm;
import org.uma.jmetal.algorithm.multiobjective.moead.AbstractMOEAD;
import org.uma.jmetal.algorithm.multiobjective.moead.MOEADBuilder;
import org.uma.jmetal.algorithm.multiobjective.nsgaii.NSGAIIBuilder;
import org.uma.jmetal.algorithm.multiobjective.smpso.SMPSOBuilder;
import org.uma.jmetal.operator.MutationOperator;
import org.uma.jmetal.operator.impl.crossover.DifferentialEvolutionCrossover;
import org.uma.jmetal.operator.impl.crossover.SBXCrossover;
import org.uma.jmetal.operator.impl.mutation.PolynomialMutation;
import org.uma.jmetal.problem.DoubleProblem;
import org.uma.jmetal.problem.Problem;
import org.uma.jmetal.qualityindicator.impl.Epsilon;
import org.uma.jmetal.qualityindicator.impl.GenerationalDistance;
import org.uma.jmetal.qualityindicator.impl.InvertedGenerationalDistance;
import org.uma.jmetal.qualityindicator.impl.InvertedGenerationalDistancePlus;
import org.uma.jmetal.qualityindicator.impl.Spread;
import org.uma.jmetal.qualityindicator.impl.hypervolume.PISAHypervolume;
import org.uma.jmetal.solution.DoubleSolution;
import org.uma.jmetal.util.JMetalException;
import org.uma.jmetal.util.archive.BoundedArchive;
import org.uma.jmetal.util.archive.impl.CrowdingDistanceArchive;
import org.uma.jmetal.util.evaluator.impl.SequentialSolutionListEvaluator;
import org.uma.jmetal.util.experiment.Experiment;
import org.uma.jmetal.util.experiment.ExperimentBuilder;
import org.uma.jmetal.util.experiment.component.ComputeQualityIndicators;
import org.uma.jmetal.util.experiment.component.ExecuteAlgorithms;
import org.uma.jmetal.util.experiment.component.GenerateBoxplotsWithR;
import org.uma.jmetal.util.experiment.component.GenerateFriedmanTestTables;
import org.uma.jmetal.util.experiment.component.GenerateLatexTablesWithStatistics;
import org.uma.jmetal.util.experiment.component.GenerateReferenceParetoFront;
import org.uma.jmetal.util.experiment.component.GenerateWilcoxonTestTablesWithR;
import org.uma.jmetal.util.experiment.util.TaggedAlgorithm;
import org.uma.jmetal.util.pseudorandom.impl.MersenneTwisterGenerator;

/**
 * Experimental study based on solving the CloudSimPowerProblemIntDouble
 * problems with three algorithms: NSGAII, MOEAD, SMPSO
 *
 * This experiment assumes that the reference Pareto front are not known, so the
 * names of files containing them and the directory where they are located must
 * be specified.
 *
 * Six quality indicators are used for performance assessment.
 *
 * The steps to carry out the experiment are: 1. Configure the experiment 2.
 * Execute the algorithms 3. Generate the reference Pareto fronts 4. Compute que
 * quality indicators 5. Generate Latex tables reporting means and medians 6.
 * Generate Latex tables with the result of applying the Wilcoxon Rank Sum Test
 * 7. Generate Latex tables with the ranking obtained by applying the Friedman
 * test 8. Generate R scripts to obtain boxplots
 *
 * @author Tarun Chhabra <tchhabr@ncsu.edu>
 */
public class AlgorithmsStudy {
	private static final int INDEPENDENT_RUNS = 20;

	public static void main(String[] args) throws IOException {
		if (args.length != 2) {
			throw new JMetalException("Needed arguments: experimentBaseDirectory referenceFrontDirectory");
		}

		String experimentBaseDirectory = args[0];
		String referenceFrontDirectory = args[1];

		List<Problem<DoubleSolution>> problemList = Arrays
				.<Problem<DoubleSolution>> asList(new CloudSimPowerProblemIntDouble());

		List<TaggedAlgorithm<List<DoubleSolution>>> algorithmList = configureAlgorithmList(problemList,
				INDEPENDENT_RUNS);

		Experiment<DoubleSolution, List<DoubleSolution>> experiment = new ExperimentBuilder<DoubleSolution, List<DoubleSolution>>(
				"CloudComputeProblemStudy").setAlgorithmList(algorithmList).setProblemList(problemList)
						.setExperimentBaseDirectory(experimentBaseDirectory).setOutputParetoFrontFileName("FUN")
						.setOutputParetoSetFileName("VAR").setReferenceFrontDirectory(referenceFrontDirectory)
						.setIndicatorList(Arrays.asList(new Epsilon<DoubleSolution>(), new Spread<DoubleSolution>(),
								new GenerationalDistance<DoubleSolution>(), new PISAHypervolume<DoubleSolution>(),
								new InvertedGenerationalDistance<DoubleSolution>(),
								new InvertedGenerationalDistancePlus<DoubleSolution>()))
						.setIndependentRuns(INDEPENDENT_RUNS).setNumberOfCores(1).build();
		new ExecuteAlgorithms<>(experiment).run();
		//experiment.setIndependentRuns(6);
		new GenerateReferenceParetoFront(experiment).run();
		new ComputeQualityIndicators<>(experiment).run();
		new GenerateLatexTablesWithStatistics(experiment).run();
		new GenerateWilcoxonTestTablesWithR<>(experiment).run();
		new GenerateFriedmanTestTables<>(experiment).run();
		new GenerateBoxplotsWithR<>(experiment).setRows(1).setColumns(2).setDisplayNotch().run();

	}

	private static List<TaggedAlgorithm<List<DoubleSolution>>> configureAlgorithmList(
			List<Problem<DoubleSolution>> problemList, int independentRuns) {
		List<TaggedAlgorithm<List<DoubleSolution>>> algorithms = new ArrayList<>();
		for (int run = 0; run < independentRuns; run++) {
			// NSGA II runs
			for (int i = 0; i < problemList.size(); i++) {
				Algorithm<List<DoubleSolution>> algorithm = new NSGAIIBuilder<>(problemList.get(i),
						new SBXCrossover(1.0, 5),
						new PolynomialMutation(1.0 / problemList.get(i).getNumberOfVariables(), 10.0))
								.setMaxEvaluations(250).setPopulationSize(100).build();
				algorithms.add(new TaggedAlgorithm<List<DoubleSolution>>(algorithm, "NSGAII", problemList.get(i), run));
			}
			// MOEAD
			for (int i = 0; i < problemList.size(); i++) {
				DifferentialEvolutionCrossover crossover;
				MutationOperator<DoubleSolution> mutation;
				double cr = 1.0;
				double f = 0.5;
				crossover = new DifferentialEvolutionCrossover(cr, f, "rand/1/bin");

				double mutationProbability = 1.0 / problemList.get(i).getNumberOfVariables();
				double mutationDistributionIndex = 20.0;
				mutation = new PolynomialMutation(mutationProbability, mutationDistributionIndex);

				Algorithm<List<DoubleSolution>> algorithm = new MOEADBuilder(problemList.get(i),
						MOEADBuilder.Variant.MOEAD).setCrossover(crossover).setMutation(mutation).setMaxEvaluations(250)
								.setPopulationSize(100).setResultPopulationSize(100)
								.setNeighborhoodSelectionProbability(0.9).setMaximumNumberOfReplacedSolutions(2)
								.setNeighborSize(20).setFunctionType(AbstractMOEAD.FunctionType.TCHE)
								.setDataDirectory("MOEAD_Weights").build();
				algorithms.add(new TaggedAlgorithm<List<DoubleSolution>>(algorithm, "MOEAD", problemList.get(i), run));

			}
			
			for (int i = 0; i < problemList.size(); i++) {
				MutationOperator<DoubleSolution> mutation;
				BoundedArchive<DoubleSolution> archive = new CrowdingDistanceArchive<DoubleSolution>(100);

				double mutationProbability = 1.0 / problemList.get(i).getNumberOfVariables();
				double mutationDistributionIndex = 20.0;
				mutation = new PolynomialMutation(mutationProbability, mutationDistributionIndex);

				Algorithm<List<DoubleSolution>> algorithm = new SMPSOBuilder((DoubleProblem) problemList.get(i),
						archive).setMutation(mutation).setMaxIterations(250).setSwarmSize(50)
								.setRandomGenerator(new MersenneTwisterGenerator())
								.setSolutionListEvaluator(new SequentialSolutionListEvaluator<DoubleSolution>())
								.build();
				algorithms.add(new TaggedAlgorithm<List<DoubleSolution>>(algorithm, "SMPSO", problemList.get(i), run));
			}
		}

		return algorithms;
	}

}
