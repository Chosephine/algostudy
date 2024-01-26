

/*
 * 프로그래머스 120897 약수 구하기
 * ArrayList -> int[]
 */


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;


public class solve052 {
	public static int[] solution(int n) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        for (int i = 1; i <= n; i++) {
        	if (n % i == 0) {
        		answer.add(i);
        	}
        }
        // ArrayList -> int[] 
        int[] ans = answer.stream().mapToInt(i -> i).toArray();
        
        return ans;
    }
	public static void main(String[] args) throws Exception {
		// 목표값 input으로 받
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int[] answer = solution(N);
		System.out.println(Arrays.toString(answer));
	}
}
