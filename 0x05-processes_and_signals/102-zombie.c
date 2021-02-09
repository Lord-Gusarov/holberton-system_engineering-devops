#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

/**
 * infinite_while - keeps a prgram open until a kill signal
 * is received
 *
 * Return: Always zero
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main -created 5 zombie processes and displays their pid
 *
 * Return: Always Zero
 */
int main(void)
{
	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid)
			printf("Zombie process created, PID: %i\n", pid);
		else
			exit(0);
		i++;
	}
	return (infinite_while());
}
