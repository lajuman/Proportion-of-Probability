import scipy.stats as stats

def proportion_of_probability(mean, sd, bottom, top):
    z_bottom = (bottom - mean) / sd
    z_top = (top - mean) / sd    
    proportion = stats.norm.cdf(z_top) - stats.norm.cdf(z_bottom)
    return proportion

print('\n---------- Proportion of Probability ----------')

mean = float(input('Mean\t? '))##########
sd = float(input('SD\t? ')) ##########
bottom = float(input('Bottom\t? ')) ##########
top = float(input('Top\t? ')) ##########
proportion = proportion_of_probability(mean, sd, bottom, top)
print(f'Proportion of Probability:  {round(proportion*100,2)}%')

print ('-'*40+'\n')
