import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 백준 9012 괄호
 * https://www.acmicpc.net/problem/9012
*/

public class solve063 {
	public static String stack(char[] PS) {
		String answer = "YES";
		
		boolean[] isOpen = new boolean[50];
		int idx = 0;
				
		for (char token : PS) {
			
			if (token == '(') {
				
				isOpen[idx] = true;
				idx += 1;
				
			} else {
				
				if (idx == 0) {
					answer = "NO";
					break;
				} else {
					idx -= 1;
				}
				
			}
		}
		
		if (idx > 0) {
			
			answer = "NO";
			
		}
		
		return answer;
	}
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < N; i ++) {
			
			System.out.println(stack(br.readLine().toCharArray()));
			
		}
		
	}

}
