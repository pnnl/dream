package objects;

import utilities.Constants;

/**
 * Formalizing the comparison of time steps
 * @author port091
 * @author rodr144
 */

public class TimeStep implements Comparable<TimeStep> {

	private volatile int timeStep;
	private volatile Float realTime;
	private volatile int realTimeInt;

	public TimeStep(int timeStep, float realTime, int realTimeInt) {
		this.timeStep = timeStep;
		this.realTime = realTime;
		this.realTimeInt = realTimeInt;
	}

	public synchronized int getTimeStep() {
		return timeStep;
	}

	public synchronized float getRealTime() {
		return realTime == null ? Float.valueOf(realTimeInt) : realTime;
	}
	
	public synchronized int getRealTimeInt() {
		return realTimeInt;
	}
	
	@Override
	public String toString() {
		return "[" + timeStep + ": " + Constants.decimalFormat.format(realTime)
				+ " yr]";
	}

	@Override
	public int compareTo(TimeStep o) {
		if(o == null) return 1;
		return Integer.valueOf(timeStep).compareTo(o.getTimeStep());
	}
}
