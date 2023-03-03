import java.util.*;

/*
 * programmers 코딩테스트 입문
 * 짝수의 합
*/

public class solve023{
	
	public static int[] solution(int[] numbers, int num1, int num2) {
		int[] answer = new int[num2 - num1 + 1];
		for (int i = num1; i <= num2; i++) {
			answer[i-num1] = numbers[i];
		}
		return answer;
		// Arrays.copyOfRange(); 메소드도 사용가능!
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int[] inPut = {1, 2, 3, 4, 5};
    	int inPut1 = 1;
    	int inPut2 = 3;
    	int[] answer = solution(inPut, inPut1, inPut2);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(String.valueOf(answer));
//    	System.out.println(answer);
    }
}
