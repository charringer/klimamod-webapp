% rebase('base.tpl', title='Tweak parameters')

<p>*tear*, *clinch*...</p>

% if taction == 'update':
%   if not bad_values:
<p>Parameters updated successfully.</p>
%   else:
<p>Shit happened.</p>
<pre>{{bad_values}}</pre>
%   end

% elif taction == 'reset':
<p>Parameters are reset.</p>

%end

<h3>Tweak parameters</h3>
<form action="/tweakparams" method="GET">
% from climath.model import Model
% for var in Model.param_keys:
  {{var}}:<br />
  <input type="text" name="{{var}}" value="" style="width: 6em;" /><br />
% end
  <input type="hidden" name="taction" value="update" />
  <input type="submit" value="Update values" />
</form>

<h3>Reset parameters</h3>
<form action="/tweakparams" method="GET">
  <input type="hidden" name="taction" value="reset" />
  <input type="submit" value="Reset to default values" />
</form>
