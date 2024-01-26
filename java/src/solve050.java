
import java.lang.StringBuilder;

/*
 * 프로그래머스 120895 인덱스 바꾸기
 * StringBuilder 써보기~
*/

public class solve050 {
    public static String solution(String my_string, int num1, int num2) {
        char[] my_chars = my_string.toCharArray();
        char temp = my_chars[num2];
        my_chars[num2] = my_chars[num1];
        my_chars[num1] = temp;
        StringBuilder sb = new StringBuilder();
        sb.append(my_chars);
        return sb.toString();
    }
    public static void main(String[] args) {
		String my_string = "hello";
		int num1  = 1;
		int num2 = 2;
		String answer = solution(my_string, num1, num2);
		System.out.println(answer);
	}
}
