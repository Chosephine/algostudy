import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 백준 27866 문자와 문자열
*/

public class solve058 {
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		int idx = Integer.parseInt(br.readLine());
		
		
		System.out.println(str.charAt(idx - 1));
		
	}
}
