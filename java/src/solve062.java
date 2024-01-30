import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/*
 * 백준 1546 평균
 * https://www.acmicpc.net/problem/1546
*/

public class solve062 {
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		// 공백 기준으로 분리하기 위한 StringTokenizer 사용
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		List<Integer> scoresList = new ArrayList<>();
		
		while (st.hasMoreTokens()) {
			
			scoresList.add(Integer.parseInt(st.nextToken()));
			
		}
		
		// Collections class를 사용하면 쉽게 max값을 구할 수 있다
		int maxScore = Collections.max(scoresList);
		
		// stream 기법을 사용해서 arrayList 합 계산
		// 우항의 모든 인자가 int여서 값이 제대로 안나와 분모 강제 타입변환 수행
		float answer = (scoresList.stream().mapToInt(Integer::intValue).sum() * 100)/(float)(N * maxScore);
		
		System.out.println(answer);
		
	}
}
