# Documentation

Some notes on comments and documentation.

## README driven development

* describe what is happening first, without writing any code
* overview, usage examples, caveats

## Make docs look good

* make something you want to read
    * choose a suitable format (sometimes a README is enough)
    * choose a suitable tool (e.g. mkdocs, sphinx, ...)
    * if you comment code, you get almost free documentation
    * choose a nice template
* document functions, classes, modules if it is not totally obvious
* never repeat what the code already says
* add specific learnings, if possible

> You may wonder what kind of comments you can find in production code (e.g. you
> may learn details about operating system distributions)

## Docstrings for quick examples

Example: [holiday.py](https://github.com/pandas-dev/pandas/blob/ddf2541df866e89150210d41c22e45eb2cf83e91/pandas/tseries/holiday.py#L146-L213)

```python
class Holiday:
    """
    Class that defines a holiday with start/end dates and rules
    for observance.
    """

    def __init__(
        self,
        name,
        year=None,
        month=None,
        day=None,
        offset=None,
        observance=None,
        start_date=None,
        end_date=None,
        days_of_week=None,
    ) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the holiday , defaults to class name
        offset : array of pandas.tseries.offsets or
                class from pandas.tseries.offsets
            computes offset from date
        observance: function
            computes when holiday is given a pandas Timestamp
        days_of_week:
            provide a tuple of days e.g  (0,1,2,3,) for Monday Through Thursday
            Monday=0,..,Sunday=6
        Examples
        --------
        >>> from dateutil.relativedelta import MO
        >>> USMemorialDay = pd.tseries.holiday.Holiday(
        ...     "Memorial Day", month=5, day=31, offset=pd.DateOffset(weekday=MO(-1))
        ... )
        >>> USMemorialDay
        Holiday: Memorial Day (month=5, day=31, offset=<DateOffset: weekday=MO(-1)>)
        >>> USLaborDay = pd.tseries.holiday.Holiday(
        ...     "Labor Day", month=9, day=1, offset=pd.DateOffset(weekday=MO(1))
        ... )
        >>> USLaborDay
        Holiday: Labor Day (month=9, day=1, offset=<DateOffset: weekday=MO(+1)>)
        >>> July3rd = pd.tseries.holiday.Holiday("July 3rd", month=7, day=3)
        >>> July3rd
        Holiday: July 3rd (month=7, day=3, )
        >>> NewYears = pd.tseries.holiday.Holiday(
        ...     "New Years Day", month=1,  day=1,
        ...      observance=pd.tseries.holiday.nearest_workday
        ... )
        >>> NewYears  # doctest: +SKIP
        Holiday: New Years Day (
            month=1, day=1, observance=<function nearest_workday at 0x66545e9bc440>
        )
        >>> July3rd = pd.tseries.holiday.Holiday(
        ...     "July 3rd", month=7, day=3,
        ...     days_of_week=(0, 1, 2, 3)
        ... )
        >>> July3rd
        Holiday: July 3rd (month=7, day=3, )
        """
``` 

## Comments

* the best code needs no comments
* be specific and record part of the "situation", maybe a decision process
* better no comment than an outdated comment
* reread code to make sure comments still make sense
* mark todo items (maybe even with names): `TODO(martin)` - this can be found in
  almost any project - helps to pick up a development thread at a later point in
  time