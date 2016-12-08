package cloudsim.power.optimization;

public class PolicyConstants {

	public static String getAllocationPolicy(int policy) {
		String policyName = "";
		switch (policy) {
		case 1:
			policyName = "iqr";
			break;
		case 2:
			policyName = "lr";
			break;
		case 3:
			policyName = "lrr";
			break;
		case 4:
			policyName = "mad";
			break;
		case 5:
			policyName = "thr";
			break;
		default:
			policyName = null;
		}
		return policyName;
	}
	
	public static String getSelectionPolicy(int policy) {
		String policyName = "";
		switch (policy) {
		case 1:
			policyName = "mc";
			break;
		case 2:
			policyName = "mmt";
			break;
		case 3:
			policyName = "mu";
			break;
		case 4:
			policyName = "rs";
			break;
		default:
			policyName = null;
		}
		return policyName;
	}
	
	

}
