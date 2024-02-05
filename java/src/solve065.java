import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

/*
 * 백준 4153 직각삼각형 
 * https://www.acmicpc.net/problem/4153
 * */

public class solve065 {
	public static String checkRightTriangle(ArrayList<Integer> arr){

		if (arr.get(2) * arr.get(2) == (arr.get(0) * arr.get(0)) + (arr.get(1) * arr.get(1))) {
			return "right";
		} else return "wrong";
	}
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while (true) {
			ArrayList<Integer> sides = new ArrayList<Integer>();
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			while (st.hasMoreTokens()) {
				sides.add(Integer.parseInt(st.nextToken()));
			}
			
			Collections.sort(sides);
			
			if (sides.get(0) == 0 & sides.get(1) == 0 & sides.get(2) == 0) break;
			
			System.out.println(checkRightTriangle(sides));
			
		}
		
		
		
		
	}
}
