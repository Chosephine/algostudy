package src;
import java.util.*;

/*
 * 모음 제거
*/

public class solve039 {
	public static boolean CheckVowel(char target) {
		char[] my_bans = {'a', 'e', 'i', 'o', 'u'};
		for (char c : my_bans){
			if (target == c) {
				return true;
			}
		}
		return false;
	}
	
    public static String solution(String my_string) {
        char[] my_chars = my_string.toCharArray();
        String answer = "";
        for (char c: my_chars){
        	// 검색하는 라이브러리가 없으면 직접 구현하면 되는거지!
            if (!CheckVowel(c)) {
            	answer += c;
            }
        }
        return answer;
    }
	public static void main(String[] args) {
		String my_string = "nice to meet you";
		String answer = solution(my_string);
		System.out.println(answer);
				
	}
}
