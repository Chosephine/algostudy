import java.util.Arrays;
import java.util.stream.Stream;

/*
 * programmers 코딩테스트 입문
 * 문자 반복 출력하기
*/


/* 
 * Other ways:
 * 1) String answer = ""; 해서 + 연산자 사용도 가능
 * 2) StringBuilder 도 사용 가능
 */

public class solve018{
	public static String solution(String my_string, int n) {
		String[] myStringArray = my_string.split("");
		String[] answer = new String[my_string.length()*n];
        int index = 0;
        for (String s : myStringArray) {
        	for (int i=0 ; i < n; i++) {
        		answer[index] = s;
        		index++;
        	}
        	
        }

//        return String.valueOf(answer.toString());
        // 이건 String 참조 위치로 반환... 왜지..
        
        String fixedAnswer = String.join("", answer);
        return fixedAnswer;
        // join 해서 새로운 String을 생성해야 제대로 반환해 준다..!


    }
//	
//	public static String solution(String my_string, int n) {
//		char[] myStringArray = my_string.toCharArray();
//		char[] answer = new char[my_string.length()*n];
//		int index = 0;
//		for (char s : myStringArray) {
//			for (int i=0 ; i < n; i++) {
//				answer[index] = s;
//				index++;
//			}
//		}
//		
//		return String.valueOf(answer);
//	}

    public static void main(String[] args) throws Exception {
        String inStr = "hello";
        int inNum = 3;
        String answer = solution(inStr, inNum);
    	System.out.println(answer);
    }
}
