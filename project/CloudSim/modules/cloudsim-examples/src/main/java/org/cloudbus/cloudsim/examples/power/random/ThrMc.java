package org.cloudbus.cloudsim.examples.power.random;

import java.io.IOException;

/**
 * A simulation of a heterogeneous power aware data center that applies the Static Threshold (THR)
 * VM allocation policy and Maximum Correlation (MC) VM selection policy.
 * 
 * The remaining configuration parameters are in the Constants and RandomConstants classes.
 * 
 * If you are using any algorithms, policies or workload included in the power package please cite
 * the following paper:
 * 
 * Anton Beloglazov, and Rajkumar Buyya, "Optimal Online Deterministic Algorithms and Adaptive
 * Heuristics for Energy and Performance Efficient Dynamic Consolidation of Virtual Machines in
 * Cloud Data Centers", Concurrency and Computation: Practice and Experience (CCPE), Volume 24,
 * Issue 13, Pages: 1397-1420, John Wiley & Sons, Ltd, New York, USA, 2012
 * 
 * @author Anton Beloglazov
 * @since Jan 5, 2012
 */
public class ThrMc {

	/**
	 * The main method.
	 * 
	 * @param args the arguments
	 * @throws IOException Signals that an I/O exception has occurred.
	 */
	public static void main(String[] args) throws IOException {
		boolean enableOutput = false;
		boolean outputToFile = false;
		String inputFolder = "";
		String outputFolder = "";
		String workload = "random"; // Random workload
		String vmAllocationPolicy = "thr"; // Static Threshold (THR) VM allocation policy
		String vmSelectionPolicy = "mc"; // Maximum Correlation (MC) VM selection policy
		String parameter = "0.8"; // the static utilization threshold

		/*
		new RandomRunner(
				enableOutput,
				outputToFile,
				inputFolder,
				outputFolder,
				workload,
				vmAllocationPolicy,
				vmSelectionPolicy,
				parameter);
				*/
		int hosts = 100;
		int vms = 100;
		if (args.length > 0 && args.length <= 3){
			hosts = Integer.parseInt(args[0]);
			if (hosts == 0)
				hosts = 100;
			vms = Integer.parseInt(args[1]);
			if (vms == 0)
				vms = 100;
			int intIsOp = Integer.parseInt(args[2]);
			if (intIsOp == 1)
				enableOutput = true;
					
		}
		
		for (int host = 1 ; host <= 1000 ; host += 200){
			for (int vm = 1; vm <= 2000 && vm <= (2 * host); vm += 200){
				RandomConstants.NUMBER_OF_VMS = vm;
				RandomConstants.NUMBER_OF_HOSTS = host;
				
				System.out.println("Host :" + RandomConstants.NUMBER_OF_HOSTS);
				System.out.println("VM : " + RandomConstants.NUMBER_OF_VMS);
				
				new RandomRunner(
						enableOutput,
						outputToFile,
						inputFolder,
						outputFolder,
						workload,
						vmAllocationPolicy,
						vmSelectionPolicy,
						parameter);
			}
		}
	}

}
