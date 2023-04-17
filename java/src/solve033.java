import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 공 던지기 
 */

public class solve033 {
	
	// =================================fail=====================================
	
	public static int solution(int[] numbers, int k) {
		int answer = 0;
		
		int n = numbers.length;
		int nd = n / 2;
		int nr = n - 2 * nd;
		
		int d = k / nd;
		int r = k - d * nd;
		
		
        if (nr == 0) {
        	// numbers 원소가 짝수개인 경우: idx 짝수인 원소만 사용
        	if (r == 0) {
        		answer = numbers[2 * (nd - 1)];
        		
        	}else {        		
        		answer = numbers[2 * (r - 1)];
        	}
        	
        } else {
        	// numbers 원소가 홀수개인 경우
        	int cycle = k % n;
        	int res = k - cycle * n;
        	if (k < n/2 + 1) {
        		// 홀수 idx 라인
        		answer = numbers[(r-1) * 2];
        	} else {
        		// 짝수 idx 라인
        		answer = numbers[(k/2) * 2 - 1];
        	}
        }
        
        return answer;
    }
	
	// =================================sucess=====================================
	
	public static int resident(int n, int d) {
		// q: quotient(몫), r: resident(나머지)
		int q = n / d;
		int r = n - d * q;
		return r;
	}
	
	public static int solution2(int[] numbers, int k) {
		int num_len = numbers.length;
		int answer = 0;
		if (resident(num_len, 2) == 0) {
			int[] candidates = new int[num_len / 2];
			for (int i = 0; i < num_len / 2; i++) {
				candidates[i] = numbers[2*i];
			}
			
			System.out.println(Arrays.toString(candidates));
			int r = resident(k-1, num_len / 2);
			answer = candidates[r];
					
		} else {
			int[] candidates = new int[num_len];
			for (int i = 0; i < (num_len + 1) / 2; i++) {
				
				candidates[i] = numbers[2*i];
				
				if (i != num_len / 2) {
					candidates[i + (num_len + 1) / 2] = numbers[2 * i + 1];
				}
			}
			
			System.out.println(Arrays.toString(candidates));
			int r = resident(k-1, num_len);
			answer = candidates[r];
			
		}
		return answer;
	}
	
	// =================================EZ=====================================
	public int solution3(int[] numbers, int k) {
        return numbers[2 * (k - 1) % numbers.length];
        // ㅂㄷㅂㄷ....
    }
	
	public static void main(String[] args) {
		int[] inPut1 = {1, 2, 3};
		int inPut2 = 3;
//		int answer = solution(inPut1, inPut2);
		int answer = solution2(inPut1, inPut2);
		System.out.println(answer);
	}
}
