

import java.util.Arrays;
import java.util.HashMap;

/*
 * 프로그래머스 120896 한 번만 등장한 문자
 * HashMap, StringBuilder, Array sort
 */

public class solve051 {
	public static String solution(String s) {
        char[] c = s.toCharArray();
        HashMap<Character, Integer> cntChar = new HashMap<>();
        
        for (char ch : c) {
        	cntChar.put(ch, cntChar.getOrDefault(ch, 0) + 1);
        }
        StringBuilder sb = new StringBuilder();
        
        for (char ch: cntChar.keySet()){
        	if (cntChar.get(ch) == 1) {
        		sb.append(ch);
        	}
        }
        char[] answer = sb.toString().toCharArray();
        Arrays.sort(answer);
        String realAnswer = new String(answer);
        return realAnswer;
    }
	
	public static void main(String[] args) {
		String in = "abcabcadc";
		String answer = solution(in);
		System.out.println(answer);
	}
}
