import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

/*
 * 백준 10814 나이순 정렬
 * https://www.acmicpc.net/problem/10814
 * */

public class solve069 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String[][] arr = new String[N][2];
		
		for (int i = 0; i < N; i++){
			
			arr[i] = br.readLine().split(" ");
			
		}
		
		Arrays.sort(arr, new Comparator<String[]>() {
			
			@Override
			public int compare(String[] s1, String[] s2) {
				return Integer.parseInt(s1[0]) - Integer.parseInt(s2[0]);
			}
			
		});
		
		for (int i = 0; i < N; i++) {
			
			System.out.println(arr[i][0] + " " + arr[i][1]);
			
		}
		
	}
}
