import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 백준 1987 소수찾기
 * https://www.acmicpc.net/problem/1978
 */

public class solve059 {
	
	public static int solution(int[] arr) {
		int cnt = 0;
		
		for (int number : arr) {
			if (number != 1) {
				int flag = 1;
				for (int i = 2; i < number; i++){
					if (number % i == 0) {
						flag = 0;
						break;
					}
				}
				cnt += flag;
			}
		}
		
		return cnt;
	}

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String[] arr = br.readLine().split(" ");
		
		int[] nums = new int[N];
		for (int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(arr[i]);
		}
		
		int answer = solution(nums);
		
		System.out.println(answer);
		
		
	}
}
