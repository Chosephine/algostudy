import java.util.*;

/*
 * programmers 코딩테스트 입문
 * 가위 바위 보
*/

public class solve029{
	// 이기는 HashMap 생성
	public static HashMap<String, String> Strategy = new HashMap<>();
	
	public static void putMap() {
		Strategy.put("2", "0");
		Strategy.put("0", "5");
		Strategy.put("5", "2");
		System.out.println(Strategy);
	}

	
	public static String solution(String rsp) {
		putMap();
		String[] rspArray = rsp.split("");
        String answer = "";
        for (String e : rspArray) {
        	answer += Strategy.get(e);
        }
        return answer;
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	String inPut = "205";
    	String answer = solution(inPut);
    	System.out.println(answer);
    }
}
