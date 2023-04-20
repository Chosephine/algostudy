package src;
import java.util.Arrays;

/*
 *  문자열 정렬하기(1) 
*/

public class solve040 {
	public static int[] solution(String my_string) {
		char[] numChar = my_string.replaceAll("[a-z]", "").toCharArray();
		int[] answer = new int[numChar.length];
		for (int i = 0; i < numChar.length; i++) {
			// char -> int 일 때, ASCII 코드로 변환
			answer[i] = (int)numChar[i] - 48;
		}
		Arrays.sort(answer);
        return answer; 
    }
	public static void main(String[] args) {
		String my_string = "hi12392";
		int[] answer = solution(my_string);
		System.out.println(Arrays.toString(answer));
	}
}
