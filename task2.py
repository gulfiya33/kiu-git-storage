def warn_the_sheep(queue):
    if queue.index('wolf') == len(queue) - 1:
        return 'Pls go away and stop eating my sheep'
    else:
        N = len(queue) - queue.index('wolf') - 1
        return f'Oi! Sheep number {N}! You are about to be eaten by a wolf!'
