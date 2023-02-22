import java.util.ArrayList;
import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 피자 나눠 먹기 2
*/

public class solve009{
	
	public static int getGcd(int n, int p) {
		int gcd = 1;
		for (int i = 2 ; i <= Math.min(n, p) ; i ++) {
			if (n % i == 0 && p % i == 0 && gcd % i != 0) {
				gcd *= i;
			}
		}
		return gcd;
	}

	public static int solution(int n) {
//        피자조각(6개)과 사람 수(n)의 최대공약수(GCD)를 찾고
//        n을 GCD로 나눠 주기
        int GCD = getGcd(n, 6);
        
        return n / GCD;
    }
    
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int inPut = 4;
    	int answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    	
    }
}
