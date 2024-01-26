
import java.util.Arrays;

/*
 * 프로그래머스 120854 배열 원소의 길
*/

public class solve044 {
	public static int[] solution(String[] strlist) {
        int[] answer = new int[strlist.length];
        for (int i=0; i < strlist.length; i++) {
        	answer[i] = strlist[i].length();
        }
        return answer;
    }
	public static void main(String[] args) {
		// String[] 할당하면서 초기화할 때 {} 활용하
		String[] strlist = {"I", "Love", "Programmers."};
		int[] answer = solution(strlist);
		System.out.println(Arrays.toString(answer));
		
	}
}
