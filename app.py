from flask import Flask, render_template, jsonify, request, session
import random
import json
import os

app = Flask(__name__)
app.secret_key = 'minds_eye_memory_2026'

SYMBOLS = ['🔥','⚡','💎','🌊','🎯','🗡️','🛡️','👁️','🌙','🦅','⚙️','🔮','🐉','💀','🌟','🎲']
SCORES_FILE = os.path.join(os.path.dirname(__file__), 'scores.json')

def load_scores():
    if not os.path.exists(SCORES_FILE):
        return {'easy': [], 'medium': [], 'hard': []}
    with open(SCORES_FILE, 'r') as f:
        return json.load(f)

def save_scores(scores):
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/new_game', methods=['POST'])
def new_game():
    data = request.json
    difficulty = data.get('difficulty', 'medium')
    counts = {'easy': 8, 'medium': 12, 'hard': 16}
    pair_count = counts.get(difficulty, 12)
    symbols = SYMBOLS[:pair_count]
    cards = []
    for i, sym in enumerate(symbols):
        cards.append({'id': i*2,   'symbol': sym, 'flipped': False, 'matched': False})
        cards.append({'id': i*2+1, 'symbol': sym, 'flipped': False, 'matched': False})
    random.shuffle(cards)
    session['cards'] = cards
    session['flipped'] = []
    session['moves'] = 0
    session['matches'] = 0
    session['pair_count'] = pair_count
    session['difficulty'] = difficulty
    session['game_over'] = False
    return jsonify(state())

@app.route('/api/flip', methods=['POST'])
def flip():
    data = request.json
    card_id = data.get('card_id')
    cards = session['cards']
    flipped = session['flipped']
    moves = session['moves']
    matches = session['matches']
    pair_count = session['pair_count']
    card = next((c for c in cards if c['id'] == card_id), None)
    if not card or card['flipped'] or card['matched'] or len(flipped) >= 2:
        return jsonify(state())
    card['flipped'] = True
    flipped.append(card_id)
    result = 'flipped'
    if len(flipped) == 2:
        moves += 1
        c1 = next(c for c in cards if c['id'] == flipped[0])
        c2 = next(c for c in cards if c['id'] == flipped[1])
        if c1['symbol'] == c2['symbol']:
            c1['matched'] = True
            c2['matched'] = True
            matches += 1
            flipped = []
            result = 'match'
            if matches == pair_count:
                session['game_over'] = True
                result = 'win'
        else:
            result = 'nomatch'
    session['cards'] = cards
    session['flipped'] = flipped
    session['moves'] = moves
    session['matches'] = matches
    s = state()
    s['result'] = result
    return jsonify(s)

@app.route('/api/unflip', methods=['POST'])
def unflip():
    cards = session['cards']
    flipped = session['flipped']
    for card_id in flipped:
        card = next((c for c in cards if c['id'] == card_id), None)
        if card and not card['matched']:
            card['flipped'] = False
    session['cards'] = cards
    session['flipped'] = []
    return jsonify(state())

@app.route('/api/scores', methods=['GET'])
def get_scores():
    return jsonify(load_scores())

@app.route('/api/scores', methods=['POST'])
def post_score():
    data = request.json
    initials = data.get('initials', '???').upper()[:3]
    moves = data.get('moves', 0)
    time_sec = data.get('time', 0)
    difficulty = data.get('difficulty', 'medium')
    scores = load_scores()
    entry = {'initials': initials, 'moves': moves, 'time': time_sec}
    scores.setdefault(difficulty, []).append(entry)
    scores[difficulty].sort(key=lambda x: (x['moves'], x['time']))
    scores[difficulty] = scores[difficulty][:10]
    save_scores(scores)
    return jsonify({'ok': True, 'scores': scores[difficulty]})

def state():
    return {
        'cards': session.get('cards', []),
        'moves': session.get('moves', 0),
        'matches': session.get('matches', 0),
        'pair_count': session.get('pair_count', 12),
        'difficulty': session.get('difficulty', 'medium'),
        'game_over': session.get('game_over', False),
        'flipped_ids': session.get('flipped', [])
    }

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
