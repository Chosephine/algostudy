
/*
 * 프로그래머스 120893 대문자와 소문자
*/

public class solve034 {
	public static String solution(String my_string) {
		char[] char_string = my_string.toCharArray();
        String answer = "";
        for(char s:char_string) {
//        	if (Character.isLowerCase(s)) {
//        		answer += Character.toUpperCase(s);
//        	} else {
//        		answer += Character.toLowerCase(s);
//        	}
        	// ASCII 활용 ('A'는 65, 'a'는 97)
        	if (s < 'a') {
        		answer += Character.toLowerCase(s);
        	} else {
        		answer += Character.toUpperCase(s);
        	}
        }
        return answer;
    }
	
	public static void main(String[] args) {
		String my_string = "abCdEfghIJ";
		String answer = solution(my_string);
		System.out.println(answer);
	}
	
	// String 순회는 안되지만 .CharAt(i); 매서드로 인덱스 접근 가능..!
}
