import java.util.*;

/*
 * programmers 코딩테스트 입문
 * 구슬을 나누는 경우의 수
*/

public class solve030{

	public static int solution(int balls, int share) {
        long answer = 1;
        long answer2 = 1;
        for (int s=1 ; s <= share; s++) {
        	answer *= balls + 1 - s;
            answer2 *= s;
        }
        
        return (int) (answer/answer2);
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int inPut1 = 5;
    	int inPut2 = 3;
    	int answer = solution(inPut1, inPut2);
    	System.out.println(answer);
    }
}
