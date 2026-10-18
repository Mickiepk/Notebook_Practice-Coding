from trie import Trie


def make(*words):
    t = Trie()
    for w in words:
        t.insert(w)
    return t


def test_basic_search_and_prefix():
    t = make("apple")
    assert t.search("apple")
    assert not t.search("app")
    assert t.starts_with("app")
    assert not t.starts_with("apx")


def test_prefix_becomes_word_after_insert():
    t = make("apple")
    t.insert("app")
    assert t.search("app")
    assert t.search("apple")


def test_longer_query_than_stored():
    t = make("app")
    assert not t.search("apple")
    assert not t.starts_with("apple")


def test_empty_trie():
    t = Trie()
    assert not t.search("a")
    assert not t.starts_with("a")
    assert t.words_with_prefix("") == []
    assert t.count_words() == 0


def test_empty_prefix_matches_everything():
    t = make("b", "a")
    assert t.starts_with("")
    assert t.words_with_prefix("") == ["a", "b"]


def test_words_with_prefix_sorted_and_includes_exact_word():
    t = make("car", "card", "care", "cat", "dog", "cart", "ca")
    assert t.words_with_prefix("car") == ["car", "card", "care", "cart"]
    assert t.words_with_prefix("ca") == ["ca", "car", "card", "care", "cart", "cat"]
    assert t.words_with_prefix("d") == ["dog"]
    assert t.words_with_prefix("x") == []


def test_insert_order_does_not_matter_for_sorting():
    t = make("zebra", "apple", "mango", "apricot")
    assert t.words_with_prefix("a") == ["apple", "apricot"]


def test_duplicate_insert_counts_once():
    t = make("go", "go", "gopher", "go")
    assert t.count_words() == 2


def test_count_words():
    t = make("a", "ab", "abc", "b")
    assert t.count_words() == 4


def test_many_words():
    t = Trie()
    words = [f"w{i}" for i in range(20_000)]
    for w in words:
        t.insert(w)
    assert t.count_words() == 20_000
    assert t.search("w19999")
    assert not t.search("w20000")
    assert len(t.words_with_prefix("w1999")) == 11  # w1999, w19990..w19999
