import pickle
import ast
from jinja2 import Environment, FileSystemLoader

# from genXML import tewiki, writePage


def getData(row,i):
	w=0
	n=0
	if not row.isna().iloc[0][39]:
		w = ast.literal_eval(row.Winner.values[0])
	else:
		w = "NaN"
	if not row.isna().iloc[0][38]:
		n = ast.literal_eval(row.Nominee.values[0])
	else:
		n = "NaN"
	data = {
		'Duration':row.Duration.values[0],
		'sound_mix':row.sound_mix.values[0],
		'colors':row.colors.values[0],
		'Votes':row.Votes.values[0],
		'Rating':row.Rating.values[0],
		'cumulative':row.cumulative.values[0],
		'production_company':row.production_company.values[0],
		'budget':row.budget.values[0],
		'opening_weekend':row.opening_weekend.values[0],
		'Gross':row.Gross.values[0],
		'IMDbID1':row.IMDbID.values[0],
		'Title2':row.Title.values[0],
		'IMDbID2':row.IMDbID.values[0],
		'IMDbID3':row.IMDbID.values[0],
		'Rated':row.Rated.values[0],
		'Genre':row.Genre.values[0],
		'Release_Year':row.Release_Year.values[0],
		'Director':row.Director.values[0],
		'writers':row.writers.values[0],
		'languages':row.languages.values[0],
		'countries':row.countries.values[0],
		'colors':row.colors.values[0],
		'film_editor':row.film_editor.values[0],
		'Winner': w,
		'Nominee': n,
		'title':row.Title.values[0],
		'id': row.IMDbID.values[0], 
		'year': row.Release_Year.values[0], 
		'genre': row.Genre.values[0],
		'stars':row.stars.values[0],
		'director':row.Director.values[0],
		'writer':row.writers.values[0],
		'producer':row.producer.values[0],
		'production_company':row.production_company.values[0],
		'composer':row.composer.values[0],
		'film_locations':row.film_locations.values[0],
		'based_on':row.based_on.values[0],
		'duration': row.Duration.values[0],
		'country': row.countries.values[0],
		'budget':row.budget.values[0],
		'languages':row.languages.values[0],
		'countries':row.countries.values[0],
		'storyline':row.storyline.values[0],
		'cinematographer':row.cinematography.values[0],
		'editor':row.film_editor.values[0],
		'rated':row.Rated.values[0],
		'Gross':row.Gross.values[0],
		'composer':row.composer.values[0],
		'sound_mix':row.sound_mix.values[0],
		'IMDbID':row.IMDbID.values[0],		
		'Title':row.Title.values[0],
        'cast':row.cast.values[0].split(';'),
		'Director':row.Director.values[0],
		'writers':row.writers.values[0],
		'producer':row.producer.values[0],
		'film_editor':row.film_editor.values[0],
		'cinematography':row.cinematography.values[0],
		'casting':row.casting.values[0],
		'production_design':row.production_design.values[0],
		'set_decoration':row.set_decoration.values[0],
		'art_design':row.art_design.values[0]
	}
	if(row.Songs.values[0] != "NaN"):
		data['Songs']=ast.literal_eval(row.Songs.values[0])
		data['lensong']=len(ast.literal_eval(row.Songs.values[0]))
		if(str(type(data['Songs'][0]))=="<class 'list'>"):
			data['songcomma']="True"
		else:
			data['songcomma']="False"
	else:
		data['Songs']=row.Songs.values[0]

	return data

def main():
	file_loader = FileSystemLoader('./templates')
	env = Environment(loader=file_loader)
	template = env.get_template('main_template.j2')

	moviesDF =pickle.load(open('./123.pkl', 'rb'))

	ids = moviesDF.IMDbID.tolist()
	ids =ids[1:2] #remove this to generate articles for all movies

	# Initiate the file object
	# fobj = open('movies.xml', 'w')
	# fobj.write(tewiki+'\n')

	for i, movieId in enumerate(ids):
		row = moviesDF.loc[moviesDF['IMDbID']==movieId]
		title = row.Title.values[0]
		text = template.render(getData(row,i))
		# print(row.isna().iloc[0][39])
		# print('*')
		# print(row)
		print(i, title)
		print(text, '\n')

if __name__ == '__main__':
	main()
