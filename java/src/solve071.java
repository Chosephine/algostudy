import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

/*
 * 백준 11866 요세푸스 문제 0
 * https://www.acmicpc.net/problem/11866
*/

public class solve071 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		String[] NK = br.readLine().split(" ");
		
		int N = Integer.parseInt(NK[0]);
		int K = Integer.parseInt(NK[1]);
		
		ArrayList<Integer> people = new ArrayList<>();
		ArrayList<Integer> yosepus = new ArrayList<>();

		for (int i = 1; i < N + 1; i++) people.add(i);
		
		
		int turnIdx = -1;
		
		while (!people.isEmpty()) {
			turnIdx = (turnIdx + K) % people.size();
			yosepus.add(people.get(turnIdx));
			people.remove(turnIdx);
			turnIdx -= 1;
			
		}
		
		
		// 출력 형식 맞추기 위해 StringBuilder 사용
		sb.append("<");
		for (int i = 0; i < N; i++) {
			sb.append(yosepus.get(i));
			if (i != N - 1) {
				sb.append(", ");
			} 
			
		}
		sb.append(">");
		
		System.out.println(sb);
		
	}
}
