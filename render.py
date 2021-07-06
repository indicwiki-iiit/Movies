import pickle
import ast
from jinja2 import Environment, FileSystemLoader

from genXML import tewiki, writePage


def getData(row,i):
	w=0
	n=0
	if row.Winner.values[0] != "NaN":
		w = ast.literal_eval(row.Winner.values[0])
	else:
		w = "NaN"
	if row.Nominee.values[0] != "NaN":
		n = ast.literal_eval(row.Nominee.values[0])
	else:
		n = "NaN"
	data = {
		'Duration':row.Duration.values[0],
		'sound_mix':row.sound_mix.values[0],
		'synopsis':row.Synopsis.values[0],
		'colors':row.colors.values[0],
		'Votes':(int)(row.Votes.values[0]),
		'Rating':row.Rating.values[0],
		'cumulative':row.cumulative.values[0],
		'production_company':row.production_company.values[0],
		'budget':row.budget.values[0],
		'opening_weekend':row.opening_weekend.values[0],
		'Gross':row.Gross.values[0],
		'Rated':row.Rated.values[0],
		'Genre':row.Genre.values[0],
		'Release_Year':(int)(row.Release_Year.values[0]),
		'Director':row.Director.values[0],
		'writers':row.writers.values[0],
		'languages':row.languages.values[0],
		'countries':row.countries.values[0],
		'colors':row.colors.values[0],
		'film_editor':row.film_editor.values[0],
		'Winner': w,
		'Nominee':n,
		'IMDbID': row.IMDbID.values[0],
		'stars':row.stars.values[0],
		'producer':row.producer.values[0],
		'composer':row.composer.values[0],
		'film_locations':row.film_locations.values[0],
		'based_on':row.based_on.values[0],
		'Duration': row.Duration.values[0],
		'countries': row.countries.values[0],
		'languages': row.languages.values[0],
		'storyline':row.storyline.values[0],
		'film_editor':row.film_editor.values[0],
		'Title':row.Title.values[0],
		'cinematography':row.cinematography.values[0],
		'casting':row.casting.values[0],
		'production_design':row.production_design.values[0],
		'set_decoration':row.set_decoration.values[0],
		'art_design':row.art_design.values[0],
		'genre_list':row.Genre.values[0].split(', '),
        'languages_list':row.languages.values[0].split(', '),
        'director_list':row.Director.values[0].split(', '),
        'writers_list':row.writers.values[0].split(', '),
        'countries_list':row.countries.values[0].split(', '),
        'colors_list':row.colors.values[0].split(', '),
        'editor_list':row.film_editor.values[0].split(', '),
        'production_list':row.production_company.values[0].split(', '),
        'composer_list':row.composer.values[0].split(', '),
        'cine_list':row.cinematography.values[0].split(', '),
		'stars_list':row.stars.values[0].split(', '),
		'trivia':row.trivia.values[0],
		'eTitle':row.eTitle.values[0],
		'distributed_by': row.distributed_by.values[0],
		'distribution_format': row.distribution_format.values[0],
		'main_subject': row.main_subject.values[0],
		'part_of_series':row.part_of_series.values[0],
		'narrative_location': row.narrative_location.values[0],
		'poster': row.poster.values[0],
		'eRated':row.eRated.values[0],
		'wikipedia_url':row.wikipedia_url.values[0],
		'wikidata_url':row.wikidata_url.values[0],
		'tagline': row.tagline.values[0],
		# 'eWinner': row.eWinner.values[0],
		# 'eNominee': row.eNominee.values[0]
	}
	eWinner = []
	eNominee = []
	if row.eWinner.values[0] != "NaN":
		eW =  ast.literal_eval(row.eWinner.values[0])
		for item in eW:
			eWinner.append(item)
	else: 
		eW = "NaN"
	if row.eNominee.values[0] != "NaN":
		eN = ast.literal_eval(row.eNominee.values[0])
		for item in eN:
			eNominee.append(item)
	else:
		eN = "NaN"


	data['eWinner'] = eWinner
	data['eNominee'] = eNominee
	if(row.Songs.values[0] != "NaN"):
		data['Songs']=ast.literal_eval(row.Songs.values[0])
		data['lensong']=len(ast.literal_eval(row.Songs.values[0]))
		if(str(type(data['Songs'][0]))=="<class 'list'>"):
			data['songcomma']="True"
		else:
			data['songcomma']="False"
	else:
		data['Songs']=row.Songs.values[0]

	if(row.cast.values[0] != "NaN"):
		# data['cast']=row.cast.values[0].split(';')
		cast_list=row.cast.values[0].split(';')
		data['cast']=[]
		for c in cast_list:
			if ':' in c:
				cast_val=c.split(':')
				data['cast'].append(cast_val[1] + " గా " + "[["+ cast_val[0] +"]]")
			else:
				data['cast'].append("[[" + c +"]]")
	else:
		data['cast']=row.cast.values[0]	
	
	if(row.stars.values[0] != 'NaN'):
		data['starslist']=row.stars.values[0]
	else:
		data['starslist']=str('NaN')
	
	if(row.writers.values[0] != 'NaN'):
		data['wri_list']=row.writers.values[0]
	else:
		data['wri_list']=str('NaN')

	if(row.producer.values[0] != 'NaN'):
		data['pro_list']=row.producer.values[0]
	else:
		data['pro_list']=str('NaN')

	if(row.languages.values[0] != 'NaN'):
		data['lang_list']=row.languages.values[0]
	else:
		data['lang_list']=str('NaN')

	if(row.composer.values[0] != 'NaN'):
		data['comp_list']=row.composer.values[0]
	else:
		data['comp_list']=str('NaN')

	if(row.cinematography.values[0] != 'NaN'):
		data['cinemat_list']=row.cinematography.values[0]
	else:
		data['cinemat_list']=str('NaN')
	
	if(row.film_editor.values[0] != 'NaN'):
		data['fe_list']=row.film_editor.values[0]
	else:
		data['fe_list']=str('NaN')

	if(row.countries.values[0] != 'NaN'):
		data['crty_list']=row.countries.values[0]
	else:
		data['crty_list']=str('NaN')

	if(row.distributed_by.values[0] != 'NaN'):
		data['d_list']=row.distributed_by.values[0]
	else:
		data['d_list']=str('NaN')

	return data

def main():
	# Load the template
	file_loader = FileSystemLoader('./Templates')
	env = Environment(loader=file_loader)
	template = env.get_template('main_template.j2')

	# Load the data (.pkl)
	moviesDF =pickle.load(open('./123.pkl', 'rb'))
	
	# Test XML generation 
	# ids = ['tt0111161','tt0252487','tt0068646','tt0050083','tt0093603','tt0468569','tt0252488','tt0167260','tt0110912','tt10888594','tt0417056','tt0096870','tt0060666','tt0421051','tt0808240','tt5988370','tt4009460','tt7886848','tt6038600','tt7221896']

	#remove this to generate articles for all movies
	ids = moviesDF.IMDbID.tolist()
	ids =ids[200:300] 

	# Initiate the file object
	fobj = open('movies.xml', 'w')
	fobj.write(tewiki+'\n')

	# Give the page_id from which you want to generate the articles in
	initial_page_id = 500000

	# Loop to grab all data from the .pkl and generate articles using the template
	for i, movieId in enumerate(ids):
		row = moviesDF.loc[moviesDF['IMDbID']==movieId]
		title = row.page_heading.values[0]
		text = template.render(getData(row,i))

		writePage(initial_page_id,title,text,fobj)
		initial_page_id += 1
		print(text, '\n')

	fobj.write('</mediawiki>')
	fobj.close()

if __name__ == '__main__':
	main()