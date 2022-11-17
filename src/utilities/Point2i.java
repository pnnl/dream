package utilities;

/**
 * 2-dimensional integer class
 * @author port091
 */

public class Point2i implements Comparable<Point2i> {

	private int i;
	private int j;
		
	public Point2i(int i, int j) {
		setI(i);
		setJ(j);
	}
	
	public Point2i(Point2i toCopy) {
		this.i = toCopy.getI();
		this.j = toCopy.getJ();
	}
	
	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("(");
		builder.append(i).append(", ");
		builder.append(j);
		builder.append(")");
		return builder.toString();
	}
	
	public int getI() {
		return i;
	}

	public void setI(int i) {
		this.i = i;
	}

	public int getJ() {
		return j;
	}

	public void setJ(int j) {
		this.j = j;
	}

	@Override
	public boolean equals(Object obj){
		if(obj == null) return false;
		Point2i pt = (Point2i) obj;
		if(this.i != pt.i) return false;
		if(this.j != pt.j) return false;
		return true;
	}
	
	@Override
	public int compareTo(Point2i pt) {
		// Compare by i
		int is = Integer.valueOf(i).compareTo(pt.getI());
		if(is != 0)
			return is;
		// Then by j
		return Integer.valueOf(j).compareTo(pt.getJ());
	}
	
	@Override
	public int hashCode(){
		int result = 5;
		result = 37*result + i;
		result = 37*result + j;
		return result;
	}
}
