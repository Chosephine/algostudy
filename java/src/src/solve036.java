package src;
import java.util.*;

/*
 * 합성수 찾기 
*/

public class solve036 {
	public static int solution(int n) {
		// 소수를 담을 ArrayList 생성, 최초값 2 추가 
		ArrayList<Integer> primes = new ArrayList<>();		
		primes.add(2);
		
		// 합성수 개수 
		int answer = 0;
		
		for (int i=3; i<=n; i++) {
			for (Integer prime : primes) {
				int q = i/prime;
				// 아니 i % prime 이 되는데 왜 이렇게....ㅋㅋㅋㅋㅋ
				int res = i - prime * q;
				
				if (res == 0) {
					answer += 1;
					break;
				}
			}
			// loop에서 break를 만나지 못했다면 i는 소수 
			primes.add(i);
		}
		
        return answer;
    }
	
	public static void main(String[] args) {
		int n = 15;
		int answer = solution(n);
		System.out.println(answer);
		
	}
}
