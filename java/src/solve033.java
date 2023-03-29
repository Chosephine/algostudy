
/*
 * programmers 코딩테스트 입문
 * 공 던지기 
 */

public class solve033 {
	
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
	
	public static void main(String[] args) {
		int[] inPut1 = {1, 2, 3, 4, 5, 6};
		int inPut2 = 5;
		int answer = solution(inPut1, inPut2);
		System.out.println(answer);
	}
}
