import java.util.*;
import java.math.BigInteger;

/*
 * programmers 코딩테스트 입문
 * 구슬을 나누는 경우의 수
*/

public class solve030{

	public static BigInteger solution(int balls, int share) {
        BigInteger answer = BigInteger.ONE;
        BigInteger answer2 = BigInteger.ONE;
        for (int s=1 ; s <= share; s++) {
        	answer = answer.multiply(BigInteger.valueOf(balls + 1 - s));
            answer2 = answer2.multiply(BigInteger.valueOf(s));
        }
        
        return answer.divide(answer2);
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int inPut1 = 30;
    	int inPut2 = 30;
    	BigInteger answer = solution(inPut1, inPut2);
    	System.out.println(answer);
    }
}
