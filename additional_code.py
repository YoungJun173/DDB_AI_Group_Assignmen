

# Helper: shorten URL for plotting (last part only)
def shorten_url(u):
    return u.split("/")[-1] if isinstance(u, str) else u

idv_plot["url_short"] = idv_plot["url"].apply(shorten_url)
rev_plot["url_short"] = rev_plot["url"].apply(shorten_url)
cnt_plot["url_short"] = cnt_plot["url"].apply(shorten_url)

# ---------- 2. Make the plots ----------

plt.figure(figsize=(12, 4))
plt.bar(idv_plot["url_short"], idv_plot["avg_idvscore"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 3 and Bottom 3 Movies by Average idvscore (Expert Reviews)")
plt.ylabel("Average idvscore")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 4))
plt.bar(rev_plot["url_short"], rev_plot["unique_reviewers"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 3 and Bottom 3 Movies by Number of Unique Reviewers")
plt.ylabel("Unique reviewers")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 4))
plt.bar(cnt_plot["url_short"], cnt_plot["review_count"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 3 and Bottom 3 Movies by Number of Reviews")
plt.ylabel("Number of reviews")
plt.tight_layout()
plt.show()
