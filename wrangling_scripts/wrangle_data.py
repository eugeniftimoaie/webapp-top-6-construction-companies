import pandas as pd
import plotly.graph_objs as go

# File to read in data and prepare plotly visualizations.
# The path to the data files are in 'data/construction_top_6_europe_2020.csv'

# prepare DataFrame with company data from csv file
df = pd.read_csv('data/construction_top_6_europe_2020.csv')

# company list of selected companies for webapp
companylist = ['vinci', 'acs', 'bouygues', 'eiffage', 'skanska', 'strabag']

def graph_income_stat(company):

    """Manipulates data for plotly visualization graph containing income statement values of one selected company
    Args:
        company name

    Returns:
        list (dict): data points with year (x-data) and revenue (y-data)
        list (dict): data points with year (x-data) and ebit (y-data)
        list (dict): data points with year (x-data) and net income (y-data)
        list (dict): data points with year (x-data) and market capitalisation (y-data)
    """
    graph = []

    graph.append(
      go.Scatter(
        x = df[df['company'] == company].year.tolist(),
        y = df[df['company'] == company].revenue.tolist(),
        mode = 'lines',
        type = 'scatter',
        name = 'Revenue',
        line = dict(color = 'royalblue', width = 2)
        )
    )

    graph.append(
      go.Scatter(
        x = df[df['company'] == company].year.tolist(),
        y = df[df['company'] == company].ebit.tolist(),
        mode = 'lines',
        type = 'scatter',
        name = 'EBIT',
        line = dict(color = 'rgb(252,141,98)', width = 2)
        )
    )

    graph.append(
      go.Scatter(
        x = df[df['company'] == company].year.tolist(),
        y = df[df['company'] == company].net_income_to_shareholders.tolist(),
        mode = 'lines',
        type = 'scatter',
        name = 'Net Profit',
        line = dict(color = 'firebrick', width = 2)
        )
    )

    graph.append(
      go.Scatter(
        x = df[df['company'] == company].year.tolist(),
        y = df[df['company'] == company].market_capitalisation_31_dec.tolist(),
        mode = 'lines',
        type = 'scatter',
        name = 'Market Capital.',
        line = dict(color = 'rgb(179,179,179)', width = 3, dash = 'dot')
        )
    )

    return graph


def graph_balance_sheet(company):

    """Manipulates data for plotly visualization graph containing balance sheet values of one selected company
    Args:
        company name

    Returns:
        list (dict): data points with year (x-data) and balance sheet total (y-data)
        list (dict): data points with year (x-data) and equity (y-data)
        list (dict): data points with year (x-data) and market capitalisation (y-data)
    """
    graph = []

    graph.append(
      go.Scatter(
        x = df[df['company'] == company].year.tolist(),
        y = df[df['company'] == company].balance_sheet_tot_31_dec.tolist(),
        mode = 'lines',
        type = 'scatter',
        name = 'Total Assets',
        line = dict(color = '#990099', width = 2)
        )
    )

    graph.append(
      go.Scatter(
        x = df[df['company'] == company].year.tolist(),
        y = df[df['company'] == company].equity_to_owner_31_dec.tolist(),
        mode = 'lines',
        type = 'scatter',
        name = 'Equity',
        line = dict(color = '#109618', width = 2)
        )
    )

    graph.append(
      go.Scatter(
        x = df[df['company'] == company].year.tolist(),
        y = df[df['company'] == company].market_capitalisation_31_dec.tolist(),
        mode = 'lines',
        type = 'scatter',
        name = 'Market Capital.',
        line = dict(color = 'rgb(179,179,179)', width = 3, dash = 'dot')
        )
    )

    return graph


def layout_one(title):

    """Formating layout for plotly visualization graph containing multiple variables of one company
    Args:
        title of graph

    Returns:
        layout configuration
    """

    layout = dict(title = title,
        legend = dict(
            orientation = 'h',
            x = -0.01,
            y = 1.16,
            font = dict(size = 10),
            ),
        xaxis = dict(
            #title = 'Year'
            showline = True,
            showgrid = True,
            showticklabels = True,
            ticks = 'outside',
            dtick = 1),
        yaxis = dict(
            #title = 'Amount [€]',
            showline = True,
            showgrid = True,
            showticklabels = True,
            ticks = 'outside',
            rangemode = 'tozero',
            autotick = True,
            ),
        )
    return layout

def layout_all(title):

    """Formating layout for plotly visualization graph containing one variables of each company
    Args:
        title of graph

    Returns:
        layout configuration
    """

    layout = dict(title = title,
        legend = dict(
            orientation = 'h',
            x = -0.01,
            y = 1.19,
            font = dict(size = 10),
            ),
        xaxis = dict(
            #title = 'Year'
            showline = True,
            showgrid = True,
            showticklabels = True,
            ticks = 'outside',
            dtick = 1),
        yaxis = dict(
            #title = 'Amount [€]',
            showline = True,
            showgrid = True,
            showticklabels = True,
            ticks = 'outside',
            rangemode = 'tozero',
            autotick = True,
            ),
        )
    return layout


def return_figures():

    """Creates plotly visualizations
    Args:
        None

    Returns:
        list (dict): list containing plotly visualizations
    """

    # chart plots: revenues of top 6 companies from 2007 to 2019 as a line chart
    graph_revenue = []

    for company in companylist:
      x_val = df[df['company'] == company].year.tolist()
      y_val = df[df['company'] == company].revenue.tolist()
      graph_revenue.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = company.upper()
          )
      )

    layout_revenue = layout_all('Trend - Revenue Top 6 Companies [€]')

    # chart plots: employees of top 6 companies from 2007 to 2019 as a line chart
    graph_employee = []

    for company in companylist:
      x_val = df[df['company'] == company].year.tolist()
      y_val = df[df['company'] == company].employees_31_dec.tolist()
      graph_employee.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = company.upper()
          )
      )

    layout_employee = layout_all('Trend - Employees Top 6 Companies')

    # chart plots: revenue, ebit and net income attributable to shareholders
    # of vinci from 2007 to 2019 as a line chart
    graph_vinci_1 = graph_income_stat(companylist[0])
    layout_vinci_1 = layout_one('Trend - Revenue | EBIT | Net Profit [€]')

    # chart plots: market capitalisation, equity and balance sheet total
    # of vinci from 2007 to 2019 as a line chart
    graph_vinci_2 = graph_balance_sheet(companylist[0])
    layout_vinci_2 = layout_one('Trend - Market Capitalisation | Equity [€]')


    # chart plots: revenue, ebit and net income attributable to shareholders
    # of ACS from 2007 to 2019 as a line chart
    graph_acs_1 = graph_income_stat(companylist[1])
    layout_acs_1 = layout_one('Trend - Revenue | EBIT | Net Profit [€]')

    # chart plots: market capitalisation, equity and balance sheet total
    # of ACS from 2007 to 2019 as a line chart
    graph_acs_2 = graph_balance_sheet(companylist[1])
    layout_acs_2 = layout_one('Trend - Market Capitalisation | Equity [€]')

    # chart plots: revenue, ebit and net income attributable to shareholders
    # of bouygues from 2007 to 2019 as a line chart
    graph_bouygues_1 = graph_income_stat(companylist[2])
    layout_bouygues_1 = layout_one('Trend - Revenue | EBIT | Net Profit [€]')

    # chart plots: market capitalisation, equity and balance sheet total
    # of bouygues from 2007 to 2019 as a line chart
    graph_bouygues_2 = graph_balance_sheet(companylist[2])
    layout_bouygues_2 = layout_one('Trend - Market Capitalisation | Equity [€]')

    # chart plots: revenue, ebit and net income attributable to shareholders
    # of eiffage from 2007 to 2019 as a line chart
    graph_eiffage_1 = graph_income_stat(companylist[3])
    layout_eiffage_1 = layout_one('Trend - Revenue | EBIT | Net Profit [€]')

    # chart plots: market capitalisation, equity and balance sheet total
    # of eiffage from 2007 to 2019 as a line chart
    graph_eiffage_2 = graph_balance_sheet(companylist[3])
    layout_eiffage_2 = layout_one('Trend - Market Capitalisation | Equity [€]')

    # chart plots: revenue, ebit and net income attributable to shareholders
    # of skanska from 2007 to 2019 as a line chart
    graph_skanska_1 = graph_income_stat(companylist[4])
    layout_skanska_1 = layout_one('Trend - Revenue | EBIT | Net Profit [€]')

    # chart plots: market capitalisation, equity and balance sheet total
    # of skanska from 2007 to 2019 as a line chart
    graph_skanska_2 = graph_balance_sheet(companylist[4])
    layout_skanska_2 = layout_one('Trend - Market Capitalisation | Equity [€]')

    # chart plots: revenue, ebit and net income attributable to shareholders
    # of skanska from 2007 to 2019 as a line chart
    graph_strabag_1 = graph_income_stat(companylist[5])
    layout_strabag_1 = layout_one('Trend - Revenue | EBIT | Net Profit [€]')

    # chart plots: market capitalisation, equity and balance sheet total
    # of skanska from 2007 to 2019 as a line chart
    graph_strabag_2 = graph_balance_sheet(companylist[5])
    layout_strabag_2 = layout_one('Trend - Market Capitalisation | Equity [€]')

    # chart plots: Net Income ratio of top 6 companies from 2007 to 2019 as a line chart
    graph_income_ratio = []

    for company in companylist:
      x_val = df[df['company'] == company].year.tolist()
      y_val = df[df['company'] == company].net_income_ratio.tolist()
      graph_income_ratio.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = company.upper()
          )
      )

    layout_income_ratio = layout_all('Trend - Net Profit Margin Top 6 Companies [%]')

    # chart plots: Equity ratio of top 6 companies from 2007 to 2019 as a line chart
    graph_equity_ratio = []

    for company in companylist:
      x_val = df[df['company'] == company].year.tolist()
      y_val = df[df['company'] == company].equity_ratio_31_dec.tolist()
      graph_equity_ratio.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = company.upper()
          )
      )

    layout_equity_ratio = layout_all('Trend - Equity Ratio Top 6 Companies [%]')

    # chart plots: Growth Revenue of top 6 companies from 2007 to 2019 as a line chart
    graph_growth_revenue = []

    for company in companylist:
      x_val = df[df['company'] == company].year.tolist()
      y_val = df[df['company'] == company].growth_revenue.tolist()
      graph_growth_revenue.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = company.upper()
          )
      )

    layout_growth_revenue = layout_all('Growth - Revenue Top 6 Companies [%]')

    # chart plots: Growth Net Income of top 6 companies from 2007 to 2019 as a line chart
    graph_growth_net_income = []

    for company in companylist:
      x_val = df[df['company'] == company].year.tolist()
      y_val = df[df['company'] == company].growth_net_income.tolist()
      graph_growth_net_income.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = company.upper()
          )
      )

    layout_growth_net_income = layout_all('Growth - Net Profit Top 6 Companies [%]')

    # chart plots: Growth Equity of top 6 companies from 2007 to 2019 as a line chart
    graph_growth_equity = []

    for company in companylist:
      x_val = df[df['company'] == company].year.tolist()
      y_val = df[df['company'] == company].growth_equity.tolist()
      graph_growth_equity.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = company.upper()
          )
      )

    layout_growth_equity = layout_all('Growth - Equity Top 6 Companies [%]')

    # chart plots: Growth Marke Capitalisation of top 6 companies from 2007 to 2019 as a line chart
    graph_growth_market_cap = []

    for company in companylist:
      x_val = df[df['company'] == company].year.tolist()
      y_val = df[df['company'] == company].growth_market_capitalisation.tolist()
      graph_growth_market_cap.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = company.upper()
          )
      )

    layout_growth_market_cap = layout_all('Growth - Market Capitalisation Top 6 Companies [%]')

    # append all charts to the figures list
    figures = []
    figures.append(dict(data = graph_revenue, layout = layout_revenue))
    figures.append(dict(data = graph_employee, layout = layout_employee))
    figures.append(dict(data = graph_vinci_1, layout = layout_vinci_1))
    figures.append(dict(data = graph_vinci_2, layout = layout_vinci_2))
    figures.append(dict(data = graph_acs_1, layout = layout_acs_1))
    figures.append(dict(data = graph_acs_2, layout = layout_acs_2))
    figures.append(dict(data = graph_bouygues_1, layout = layout_bouygues_1))
    figures.append(dict(data = graph_bouygues_2, layout = layout_bouygues_2))
    figures.append(dict(data = graph_eiffage_1, layout = layout_eiffage_1))
    figures.append(dict(data = graph_eiffage_2, layout = layout_eiffage_2))
    figures.append(dict(data = graph_skanska_1, layout = layout_skanska_1))
    figures.append(dict(data = graph_skanska_2, layout = layout_skanska_2))
    figures.append(dict(data = graph_strabag_1, layout = layout_strabag_1))
    figures.append(dict(data = graph_strabag_2, layout = layout_strabag_2))
    figures.append(dict(data = graph_income_ratio, layout = layout_income_ratio))
    figures.append(dict(data = graph_equity_ratio, layout = layout_equity_ratio))
    figures.append(dict(data = graph_growth_revenue, layout = layout_growth_revenue))
    figures.append(dict(data = graph_growth_net_income, layout = layout_growth_net_income))
    figures.append(dict(data = graph_growth_equity, layout = layout_growth_equity))
    figures.append(dict(data = graph_growth_market_cap, layout = layout_growth_market_cap))

    return figures
