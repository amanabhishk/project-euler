#include <stdio.h>
using namespace std;

int points[] = {2,3,6,7,8};
long long res[100001];

void ways(int m, int total)
{
	res[0] = 1;

	for (int i=0; i<m; i++)
		for (int j=points[i]; j<=total; j++)
			res[j] += res[j-points[i]];
}

int main()
{
	int n;
	ways (5, 100000);
	scanf ("%d", &n);
	while (n--)
	{
		int s;
		scanf ("%d", &s);
		printf ("%lld\n", res[s]);
	}
}