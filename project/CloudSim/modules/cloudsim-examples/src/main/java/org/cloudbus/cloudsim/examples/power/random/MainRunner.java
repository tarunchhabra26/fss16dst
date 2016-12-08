package org.cloudbus.cloudsim.examples.power.random;

import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.cloudbus.cloudsim.examples.power.Constants;
import org.cloudbus.cloudsim.examples.power.Helper;
import org.cloudbus.cloudsim.power.PowerDatacenter;
import org.cloudbus.cloudsim.util.MathUtil;

public class MainRunner {
	
	public static final String ENERGY_CONSUMPTION = "energy";
	public static final String AVERAGE_SLA = "sla";
	public static final String MEAN_HOST_SHUTDOWN_TIME = "shutdown";

	private static boolean enableOutput;
	private static boolean outputToFile;
	private String inputFolder = "";
	private String outputFolder = "";
	private String workload = "random"; // Random workload

	public String getInputFolder() {
		return inputFolder;
	}

	public void setInputFolder(String inputFolder) {
		this.inputFolder = inputFolder;
	}

	public String getOutputFolder() {
		return outputFolder;
	}

	public void setOutputFolder(String outputFolder) {
		this.outputFolder = outputFolder;
	}

	public String getWorkload() {
		return workload;
	}

	public void setWorkload(String workload) {
		this.workload = workload;
	}

	public MainRunner(boolean enableOuput, boolean outputToFile, String inputFolder, String outputFolder) {
		MainRunner.enableOutput = enableOuput;
		MainRunner.outputToFile = outputToFile;
		this.inputFolder = inputFolder;
		this.outputFolder = outputFolder;
	}

	public Map<String, Double> genericRunner(String vmAllocationPolicy, String vmSelectionPolicy, String parameter,
			int hosts, int vms, int[] vmPes, int[] vmMips, int[] vmRam, int[] hostPes, int[] hostMips, int[] hostRam,
			int hostBw, int hostStorage, int vmBm, int hostType, int vmTypes) throws IOException {
		
		String workload = "random";
		Constants.CLOUDLET_PES = 1;
		RandomConstants.NUMBER_OF_HOSTS = hosts;
		RandomConstants.NUMBER_OF_VMS = vms;
		Constants.VM_PES = vmPes;
		Constants.VM_MIPS = vmMips;
		Constants.VM_RAM = vmRam;
		Constants.HOST_PES = hostPes;
		Constants.HOST_MIPS = hostMips;
		Constants.HOST_RAM = hostRam;
		Constants.HOST_BW = hostBw;
		Constants.HOST_STORAGE = hostStorage;
		Constants.VM_BW = vmBm;
		Constants.HOST_TYPES = hostType;
		Constants.VM_TYPES = vmTypes;
		
		System.out.println("Host :" + RandomConstants.NUMBER_OF_HOSTS);
		System.out.println("VM : " + RandomConstants.NUMBER_OF_VMS);
		System.out.println("Parameter : " + parameter);
		System.out.println("vmAllocationPolicy : " + vmAllocationPolicy);
		System.out.println("vmSelectionPolicy : " + vmSelectionPolicy);
		System.out.println("vmPes : " + Arrays.toString(vmPes));
		System.out.println("vmMips : " + Arrays.toString(vmMips));
		System.out.println("vmRam : " + Arrays.toString(vmRam));
		System.out.println("hostPes : " + Arrays.toString(hostPes));
		System.out.println("hostMips : " + Arrays.toString(hostMips));
		System.out.println("hostRam : " + Arrays.toString(hostRam));
		System.out.println("hostBw : " + hostBw);
		System.out.println("hostStorage : " + hostStorage);
		System.out.println("vmBm : " + vmBm);
		System.out.println("hostType : " + hostType);
		System.out.println("vmTypes : " + vmTypes);
		
		long start = System.currentTimeMillis();
		RandomRunner runner = new RandomRunner(enableOutput, outputToFile, inputFolder, outputFolder, workload,
				vmAllocationPolicy, vmSelectionPolicy, parameter);
		long end = System.currentTimeMillis();
		System.out.println("\nTotal simulation time : " + (end - start) + " ms");

		PowerDatacenter datacenter = runner.getmDataCenter();
		
		Map<String, Double> objectiveScores = new HashMap<String,Double>();
		Map<String, Double> slaMetrics = Helper.getSlaMetrics(runner.getVmList());
		double slaAverage = slaMetrics.get("average");
		objectiveScores.put(AVERAGE_SLA, slaAverage);
		
		List<Double> timeBeforeHostShutdown = Helper.getTimesBeforeHostShutdown(datacenter.getHostList());
		
		double meanTimeBeforeHostShutdown = Double.NaN;
		if (!timeBeforeHostShutdown.isEmpty()) {
			meanTimeBeforeHostShutdown = MathUtil.mean(timeBeforeHostShutdown);
		}
		objectiveScores.put(MEAN_HOST_SHUTDOWN_TIME, meanTimeBeforeHostShutdown);
		
		double energy = datacenter.getPower() / (3600 * 1000);
		
		objectiveScores.put(ENERGY_CONSUMPTION, energy);
		if (objectiveScores.size() > 0)
			return objectiveScores;
		else
			return null;
	}

	/**
	 * The main method just for testing.
	 * 
	 * @param args
	 *            the arguments
	 * @throws IOException
	 *             Signals that an I/O exception has occurred.
	 */
	
	public static void main(String[] args) throws IOException {
		int[] vmPes = {1, 1};
		int[] vmMips = {2500, 100};
		int[] vmRam = {870, 1740};
		int[] hostPes = {2, 2};
		int[] hostMips = {1860, 5000};
		int[] hostRam = {4096, 4096};
		
		MainRunner runner = new MainRunner(true, false, "", "");
		runner.genericRunner("lr", "mu", "1.393674679793466", 49, 97, vmPes, vmMips, vmRam, hostPes, hostMips, hostRam, 870291, 1074982, 129904, 2, 2);
		
		/*
		// Default parameters
		enableOutput = true;
		outputToFile = false;
		String inputFolder = "";
		String outputFolder = "../output";
		String workload = "random"; // Random workload
		String vmAllocationPolicy = "thr"; // Static Threshold (THR) VM
											// allocation policy
		String vmSelectionPolicy = "mc"; // Maximum Correlation (MC) VM
											// selection policy
		String parameter = "0.8"; // the static utilization threshold
		int hosts = 100;
		int vms = 200;
		int[] intVmPes = null;
		int[] intVmMips = null;
		int[] intVmRam = null;
		int[] intHostPes = null;
		int[] intHostMips = null;
		int[] intHostRam = null;

		if (args.length > 0) {

			workload = args[0];
			vmAllocationPolicy = args[1];
			vmSelectionPolicy = args[2];
			parameter = args[3];
			hosts = Integer.parseInt(args[4]);
			vms = Integer.parseInt(args[5]);
			Constants.NUMBER_OF_CLOUDLETS = Integer.parseInt(args[6]);
			Constants.CLOUDLET_PES = Integer.parseInt(args[7]);
			Constants.VM_TYPES = Integer.parseInt(args[8]);
			String vmPes = args[9];
			String vmMips = args[10];
			String vmRam = args[11];
			Constants.VM_BW = Integer.parseInt(args[12]);
			Constants.VM_SIZE = Integer.parseInt(args[13]);
			Constants.HOST_TYPES = Integer.parseInt(args[14]);
			String hostMips = args[15];
			String hostPes = args[16];
			String hostRam = args[17];
			Constants.HOST_BW = Integer.parseInt(args[18]);
			Constants.HOST_STORAGE = Integer.parseInt(args[19]);

			intHostPes = new int[Constants.HOST_TYPES];
			intHostMips = new int[Constants.HOST_TYPES];
			intHostRam = new int[Constants.HOST_TYPES];

			for (int i = 0; i < Constants.HOST_TYPES; i++) {
				intHostPes[i] = Integer.parseInt(hostPes.split(",")[i].trim());
				intHostMips[i] = Integer.parseInt(hostMips.split(",")[i].trim());
				intHostRam[i] = Integer.parseInt(hostRam.split(",")[i].trim());
			}

			intVmPes = new int[Constants.VM_TYPES];
			intVmMips = new int[Constants.VM_TYPES];
			intVmRam = new int[Constants.VM_TYPES];

			for (int i = 0; i < Constants.VM_TYPES; i++) {
				intVmPes[i] = Integer.parseInt(vmPes.split(",")[i].trim());
				intVmMips[i] = Integer.parseInt(vmMips.split(",")[i].trim());
				intVmRam[i] = Integer.parseInt(vmRam.split(",")[i].trim());
			}

			// Constants.VM_MIPS = intVmMips;
			Constants.VM_PES = intVmPes;
			Constants.VM_RAM = intVmRam;
			// Constants.HOST_MIPS = intHostMips;
			Constants.HOST_PES = intHostPes;
			Constants.HOST_RAM = intHostRam;

		}

		RandomConstants.NUMBER_OF_HOSTS = hosts;
		RandomConstants.NUMBER_OF_VMS = vms;

		System.out.println("Host :" + RandomConstants.NUMBER_OF_HOSTS);
		System.out.println("VM : " + RandomConstants.NUMBER_OF_VMS);

		long start = System.currentTimeMillis();
		RandomRunner runner = new RandomRunner(enableOutput, outputToFile, inputFolder, outputFolder, workload,
				vmAllocationPolicy, vmSelectionPolicy, parameter);
		long end = System.currentTimeMillis();
		System.out.println("\nTotal simulation time : " + (end - start) + " ms");

		PowerDatacenter datacenter = runner.getmDataCenter();
		double lastClock = runner.getMlastClock();

		Helper.printResults(datacenter, runner.getVmList(), lastClock, "", false, "");

		*/
	
	}

	
	

}
