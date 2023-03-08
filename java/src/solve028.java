import java.util.*;

/*
 * programmers 코딩테스트 입문
 * 모스부호(1)
*/

public class solve028{
	// 모스부호 해독해 주는 HashMap 생성
	public static HashMap<String, Character> Morse = new HashMap<>();
	
	public static void putMap() {
		// a~z에 해당하는 모스부호가 담긴 배열 활용해서 HashMap 채우는 작업자동화
		String[] morseArray = {
				".-","-...","-.-.","-..",".","..-.","--.","....",
				"..",".---","-.-",".-..","--","-.","---",".--.",
				"--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."
				};
		for (int i=0 ; i < morseArray.length ; i++) {
			// 유니코드 활용하면편리하게 담을 수 있다!
			// A: 65, a: 97
			Morse.put(morseArray[i], (char)(i + 97));
		}
		System.out.println(Morse);
	}

	
	public static String solution(String letter) {
		// HashMap 담는 함수 실행
		putMap();
		// 정답 변수 초기화
        String answer = "";
        // 공백 기준으로 letter 배열화
        String[] parsedLetter = letter.split(" ");
        
        for (String l : parsedLetter) {
        	answer += Morse.get(l);
    	}
        
        return answer;
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	String inPut = ".--. -.-- - .... --- -.";
    	String answer = solution(inPut);
    	System.out.println(answer);
    }
}
