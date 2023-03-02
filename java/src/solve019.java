
/*
 * programmers 코딩테스트 입문
 * 특정 문자 제거하기
*/

public class solve019{
	
	public static String solution(String my_string, String letter) {
        StringBuilder answer = new StringBuilder();
        String[] myString = my_string.split("");
        for (String s : myString) {
        	if (!s.equals(letter)) {
        		answer.append(s);
        	}
        }
        return answer.toString();
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	String inPut = "abcdef";
    	String eliminate = "f";
    	String answer = solution(inPut, eliminate);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    }
}
