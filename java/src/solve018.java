import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 짝수 홀수 개수
*/

public class solve018{
	public static int[] solution(int[] num_list) {
        int[] answer = {0, 0};
        for (int num : num_list) {
        	if (num % 2 == 0) {
        		answer[0] += 1;
        		// answer[0]++; 와 동일하다!
        	} else {
        		answer[1] += 1;
        	}
        }
        return answer;
    }

    public static void main(String[] args) throws Exception {
        int[] inPut = {1, 3, 5, 7};
        int[] answer = solution(inPut);
    	System.out.println(Arrays.toString(answer));
    }
}
