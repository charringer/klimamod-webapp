% rebase('base.tpl', title='Numerical simulation of '+model.name+'\'s model')

<form action="/run/{{model.modelid}}" method="GET">
  <p>
    Enter initial temperature:
    <input type="text" name="initval" value="" style="width: 6em;" />
  </p>

% for key, value in url_params.items():
  <input type="hidden" name="{{key}}" value="{{value}}" />
% end
  <input type="submit" value="Run simulation" />
</form>
