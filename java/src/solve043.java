

/*
 * 프로그래머스 120853 컨트롤 제트
*/

public class solve043 {
	public static int solution(String s) {
		String[] strArray = s.split(" ");
		int answer = 0;
		for (int i=0; i < strArray.length; i++) {
			if (!strArray[i].contentEquals("Z")) {
				// String은 참조형이기 때문에 == 가 아니라 equal 메소드로 비교해야 함!!!
				answer += Integer.parseInt(strArray[i]);
			} else {
				answer -= Integer.parseInt(strArray[i-1]);
			}
		}
        return answer;
    }
	public static void main(String[] args) {
		String s = "-1 -2 -3 Z";
		int answer = solution(s);
		System.out.println(answer);
	}
}
