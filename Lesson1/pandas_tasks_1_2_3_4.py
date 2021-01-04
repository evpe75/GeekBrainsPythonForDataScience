{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Задание 1\n",
    "# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, \n",
    "# в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].\n",
    "# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные: \n",
    "# [1, 1, 1, 2, 2, 3, 3], \n",
    "# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],\n",
    "# min.\n",
    "\n",
    "# Задание 2\n",
    "# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.\n",
    "\n",
    "# Задание 3\n",
    "# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.\n",
    "\n",
    "# Задание 4\n",
    "# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:\n",
    "# author_name, min_price, max_price и mean_price,\n",
    "# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора .\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Задание 1\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>author_id</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>7.000000</td>\n",
       "      <td>7.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1.857143</td>\n",
       "      <td>167.142857</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.899735</td>\n",
       "      <td>53.763149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>90.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>135.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>170.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2.500000</td>\n",
       "      <td>195.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>250.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       author_id       price\n",
       "count   7.000000    7.000000\n",
       "mean    1.857143  167.142857\n",
       "std     0.899735   53.763149\n",
       "min     1.000000   90.000000\n",
       "25%     1.000000  135.000000\n",
       "50%     2.000000  170.000000\n",
       "75%     2.500000  195.000000\n",
       "max     3.000000  250.000000"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = {\"author_id\": [1, 2, 3],\n",
    "     \"author_name\": ['Тургенев', 'Чехов', 'Островский']}\n",
    "\n",
    "authors = pd.DataFrame(a)\n",
    "\n",
    "b = {\"author_id\": [1, 1, 1, 2, 2, 3, 3],\n",
    "     \"book_title\": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],\n",
    "     \"price\": [250, 150, 180, 120, 170, 90, 210]}\n",
    "\n",
    "book = pd.DataFrame(b)\n",
    "\n",
    "book.describe()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   author_id author_name            book_title  price\n",
      "0          1    Тургенев           Отцы и дети    250\n",
      "1          1    Тургенев                 Рудин    150\n",
      "2          1    Тургенев     Дворянское гнездо    180\n",
      "3          2       Чехов      Толстый и тонкий    120\n",
      "4          2       Чехов       Дама с собачкой    170\n",
      "5          3  Островский                 Гроза     90\n",
      "6          3  Островский  Таланты и поклонники    210\n"
     ]
    }
   ],
   "source": [
    "# Задание 2\n",
    "authors_price = pd.merge(authors, book, on='author_id', how='inner')\n",
    "\n",
    "print(authors_price)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>author_id</th>\n",
       "      <th>author_name</th>\n",
       "      <th>book_title</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Тургенев</td>\n",
       "      <td>Отцы и дети</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>Островский</td>\n",
       "      <td>Таланты и поклонники</td>\n",
       "      <td>210</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>Тургенев</td>\n",
       "      <td>Дворянское гнездо</td>\n",
       "      <td>180</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>Чехов</td>\n",
       "      <td>Дама с собачкой</td>\n",
       "      <td>170</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>Тургенев</td>\n",
       "      <td>Рудин</td>\n",
       "      <td>150</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   author_id author_name            book_title  price\n",
       "0          1    Тургенев           Отцы и дети    250\n",
       "1          3  Островский  Таланты и поклонники    210\n",
       "2          1    Тургенев     Дворянское гнездо    180\n",
       "3          2       Чехов       Дама с собачкой    170\n",
       "4          1    Тургенев                 Рудин    150"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Задание 3\n",
    "\n",
    "authors_price.sort_values(by=\"price\", inplace=True)\n",
    "authors_price.reset_index(drop=True, inplace=True)\n",
    "\n",
    "top5 = authors_price.nlargest(5, \"price\").copy()\n",
    "top5.reset_index(drop=True, inplace=True)\n",
    "print(top5)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   author_id author_name  min_price  max_price  mean_price\n",
      "0          1    Тургенев        150        250  193.333333\n",
      "1          2       Чехов        120        170  145.000000\n",
      "2          3  Островский         90        210  150.000000\n"
     ]
    }
   ],
   "source": [
    "# Задание 4\n",
    "groupby = authors_price.groupby(\"author_id\")\n",
    "\n",
    "groupby_min = groupby.agg({\"price\": \"min\"}).copy()\n",
    "groupby_min.reset_index(drop=False, inplace=True)\n",
    "authors_min = pd.DataFrame(\n",
    "    {\"author_id\": list(groupby_min[\"author_id\"]),\n",
    "     \"min_price\": list(groupby_min[\"price\"])}\n",
    ")\n",
    "#print(authors_min)\n",
    "\n",
    "groupby_max = groupby.agg({\"price\": \"max\"}).copy()\n",
    "groupby_max.reset_index(drop=False, inplace=True)\n",
    "authors_max = pd.DataFrame(\n",
    "    {\"author_id\": list(groupby_max[\"author_id\"]),\n",
    "     \"max_price\": list(groupby_max[\"price\"])}\n",
    ")\n",
    "#print(authors_max)\n",
    "\n",
    "groupby_mean = groupby.agg({\"price\": \"mean\"}).copy()\n",
    "groupby_mean.reset_index(drop=False, inplace=True)\n",
    "authors_mean = pd.DataFrame(\n",
    "    {\"author_id\": list(groupby_mean[\"author_id\"]),\n",
    "     \"mean_price\": list(groupby_mean[\"price\"])}\n",
    ")\n",
    "#print(authors_mean)\n",
    "\n",
    "authors_stat = pd.merge(pd.merge(pd.merge(authors, authors_min, on='author_id', how='inner'), authors_max, on='author_id', how='inner'), authors_mean, on='author_id', how='inner') \n",
    "print(authors_stat)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
