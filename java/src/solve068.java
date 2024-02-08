import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 백준 1259 팰린드롬수
 * https://www.acmicpc.net/problem/1259
*/

public class solve068 {
	public static String palindrome(char[] arr) {
		
		int len = arr.length;
		
		for (int i = 0; i <= len / 2; i++) {
			
			if (arr[i] != arr[len - 1 - i]) {
				return "no";
			}
			
		}
		
		return "yes"; 
		
	}
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while (true) {
			String target = br.readLine();
			
			if (target.equals("0")) {
				
				break;
				
			}
			
			System.out.println(palindrome(target.toCharArray()));
		}
	}
}
