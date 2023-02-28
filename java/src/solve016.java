import java.util.ArrayList;
import java.util.Arrays;

/*
 * programmers 코딩테스트 입문
 * 문자열 뒤집기
*/

public class solve016{
	
	public static String solution(String my_string) {
        String answer = "";
        
        for (int i = 0; i < my_string.length(); i++) {
        	answer = my_string.charAt(i) + answer;
        	// index 마지막부터 역순으로 탐색해도 됨!
        	// StringBuilder이라는 클래스도 써보기
        }
        
        return answer;
    }

    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	String inPut = "bread";
//    	int people = 12;
    	String answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    }
}
