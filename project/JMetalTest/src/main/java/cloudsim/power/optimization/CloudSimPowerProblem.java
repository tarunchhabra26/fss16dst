package cloudsim.power.optimization;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.cloudbus.cloudsim.examples.power.random.MainRunner;
import org.uma.jmetal.problem.ConstrainedProblem;
import org.uma.jmetal.problem.impl.AbstractDoubleProblem;
import org.uma.jmetal.solution.DoubleSolution;
import org.uma.jmetal.util.solutionattribute.impl.NumberOfViolatedConstraints;
import org.uma.jmetal.util.solutionattribute.impl.OverallConstraintViolation;

public class CloudSimPowerProblem extends AbstractDoubleProblem implements ConstrainedProblem<DoubleSolution> {
	public OverallConstraintViolation<DoubleSolution> overallConstraintViolationDegree;
	public NumberOfViolatedConstraints<DoubleSolution> numberOfViolatedConstraints;

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public CloudSimPowerProblem() {
		setNumberOfVariables(10);
		setNumberOfObjectives(3);
		setNumberOfConstraints(1);
		setName("CloudSimPower");

		List<Double> lowerLimit = new ArrayList<Double>(getNumberOfVariables());
		List<Double> upperLimit = new ArrayList<Double>(getNumberOfVariables());

		// Limit for hosts 0
		lowerLimit.add(2.0);
		upperLimit.add(100.0);

		// Limit for VMs 1 -- Constrained
		lowerLimit.add(1.0);
		upperLimit.add(200.0);

		// Limit for VM Types 2
		lowerLimit.add(1.0);
		upperLimit.add(2.0);

		// Limit for Host Types 3
		lowerLimit.add(1.0);
		upperLimit.add(2.0);

		// Limit for VM Allocation Policy 4
		lowerLimit.add(1.0);
		upperLimit.add(5.0);

		// Limit for VM Selection Policy 5
		lowerLimit.add(1.0);
		upperLimit.add(4.0);

		// Limit for Utilization Policy 6
		lowerLimit.add(0.8);
		upperLimit.add(2.5);

		// Limit for VM Bandwidth 7
		lowerLimit.add(100000.0);
		upperLimit.add(200000.0);

		// Limit for Host Bandwidth 8
		lowerLimit.add(500000.0);
		upperLimit.add(1000000.0);

		// Limit for Host Storage 9
		lowerLimit.add(1000000.0);
		upperLimit.add(2000000.0);

		setLowerLimit(lowerLimit);
		setUpperLimit(upperLimit);

		overallConstraintViolationDegree = new OverallConstraintViolation<DoubleSolution>();
		numberOfViolatedConstraints = new NumberOfViolatedConstraints<DoubleSolution>();

	}

	private void finish(DoubleSolution solution, Map<String, Double> objectives) {
		solution.setObjective(0, objectives.get(MainRunner.ENERGY_CONSUMPTION));
		solution.setObjective(1, objectives.get(MainRunner.AVERAGE_SLA));
		solution.setObjective(2, -(objectives.get(MainRunner.MEAN_HOST_SHUTDOWN_TIME)));
		System.out.println("Finished with energy : " + objectives.get(MainRunner.ENERGY_CONSUMPTION)
				+ " average SLA violation : " + objectives.get(MainRunner.AVERAGE_SLA) + " mean host shutdown time : "
				+ objectives.get(MainRunner.MEAN_HOST_SHUTDOWN_TIME));
	}

	public void evaluate(DoubleSolution solution) {
		// invoke model here
		MainRunner runner = new MainRunner(true, false, "", "");
		int vmAllocationPolicy = solution.getVariableValue(4).intValue();
		int vmSelectionPolicy = solution.getVariableValue(5).intValue();
		double parameter = solution.getVariableValue(6);
		int hosts = solution.getVariableValue(0).intValue();
		int vms = solution.getVariableValue(1).intValue();
		int vmType = solution.getVariableValue(2).intValue();
		int hostType = solution.getVariableValue(3).intValue();
		int[] vmPes = { 2, 2, 2, 2 };
		int[] vmMips = { 2500, 2000, 100, 500 };
		int[] vmRam = { 870, 1740, 1740, 613 };
		int[] hostPes = { 2, 2, 4, 4 };
		int[] hostMips = { 3000, 2660, 5000, 6000 };
		int[] hostRam = { 4096, 4096, 8192, 8192 };
		int actualVmType = 4;
		int actualHostType = 4;

		if (vmType == 1) {
			vmPes[0] = 1;
			vmPes[1] = 1;
			vmMips[0] = 2500;
			vmMips[1] = 100;
			vmRam[0] = 870;
			vmRam[1] = 1740;
			actualVmType = 2;
		}

		if (hostType == 1) {
			hostPes[0] = 2;
			hostPes[1] = 2;
			hostMips[0] = 3000;
			hostMips[1] = 5000;
			hostRam[0] = 4096;
			hostRam[1] = 4096;
			actualHostType = 2;
		}

		int vmBm = solution.getVariableValue(7).intValue();
		int hostBw = solution.getVariableValue(8).intValue();
		int hostStorage = solution.getVariableValue(9).intValue();

		try {
			if (vms <= 2 * hosts) {
				// Do nothing
			} else {
				solution.setVariableValue(1, (double)hosts*2);
				vms = solution.getVariableValue(1).intValue();
			}
			Map<String, Double> objectiveResults = runner.genericRunner(
					PolicyConstants.getAllocationPolicy(vmAllocationPolicy),
					PolicyConstants.getSelectionPolicy(vmSelectionPolicy), parameter + "", hosts, vms, vmPes,
					vmMips, vmRam, hostPes, hostMips, hostRam, hostBw, hostStorage, vmBm, actualHostType,
					actualVmType);
			finish(solution, objectiveResults);
			
		} catch (IOException e) {
			System.out.println("Something falied in the model :");
			e.printStackTrace();
		}

	}

	public void evaluateConstraints(DoubleSolution solution) {
		boolean[] constraint = new boolean[this.getNumberOfConstraints()];
		int hosts = solution.getVariableValue(0).intValue();
		int vms = solution.getVariableValue(1).intValue();

		boolean isConstraintValid = false;
		if (vms <= 2 * hosts) {
			isConstraintValid = true;
		} else {
			solution.setVariableValue(1, (double)hosts*2);
		}
		constraint[0] = isConstraintValid;
		double overallConstraintViolation = 0.0;
		int violatedConstraints = 0;
		for (int i = 0; i < getNumberOfConstraints(); i++) {
			if (constraint[i] == false) {
				overallConstraintViolation += 1;
				violatedConstraints++;
			}
		}

		overallConstraintViolationDegree.setAttribute(solution, overallConstraintViolation);
		numberOfViolatedConstraints.setAttribute(solution, violatedConstraints);

	}
}
