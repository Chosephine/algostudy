import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 배열 두 배 만들기
*/

public class solve004{
	
	public static int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        for (int i=0; i < numbers.length ; i++) {
        	answer[i] = 2 * numbers[i];
        }
        return answer;
    }
    
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int[] inPut = {1, 2, 3, 4, 5};
    	int[] answer = solution(inPut);
    	System.out.printf(Arrays.toString(answer));
    	
    }
}
