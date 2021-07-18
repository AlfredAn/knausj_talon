open {user.website}: user.open_url(website)
open (r | are) slash <user.text>$: user.open_subreddit(user.text)
{user.search_engine} hunt <user.text>$: user.search_with_search_engine(search_engine, user.text)
{user.search_engine} (that|this):
    text = edit.selected_text()
    user.search_with_search_engine(search_engine, text)
