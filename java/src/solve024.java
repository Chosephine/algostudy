import java.util.*;

/*
 * programmers 코딩테스트 입문
 * 짝수의 합
*/

public class solve024{
	
	public static String solution(int age) {
        String answer = "";
        
        for (int i=3; i >= 0; i--) {
        	int digit = (int) Math.pow(10, i);
        	int q = age / digit;
        	age %= digit;
        	
        	if(answer.length() > 0 | q > 0) {
        		System.out.println((char)(97 + q));
        		answer += String.valueOf((char)(97 + q));
        	}
        }
        return answer;
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int inPut = 100;
//    	int inPut2 = 3;
    	String answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    }
}
