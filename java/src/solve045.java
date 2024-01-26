
import java.util.*;

/*
 * 프로그래머스 120888 중복된 문자 제거
*/

public class solve045 {
	public static String solution(String my_string) {
		String answer = "";
        ArrayList<Character> ans = new ArrayList<Character>();
        char[] myCharArray = my_string.toCharArray();
        for (char c: myCharArray) {
        	if (!ans.contains(c)) {
        		ans.add(c);
        		answer += c;
        	}
        }
        
        return answer;
    }
	public static void main(String[] args) {
		String my_string = "We are the world";
		String answer = solution(my_string);
		System.out.println(answer);
	}
}
