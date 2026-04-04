import base64
from .utils import xor_encrypt

def encrypt_runtime(input_path, output_path, key):
    with open(input_path, "rb") as f:
        data = f.read()

    encrypted = xor_encrypt(data, key)
    encoded = base64.b64encode(encrypted).decode("utf-8")

    lua_loader = f'''
-- 🔒 NullFox Runtime 😈
local _k = "{key}"
local _d = "{encoded}"

local function _xor(s, k)
  local out = ""
  for i = 1, #s do
    local kc = k:byte((i-1)%#k+1)
    local sc = s:byte(i)
    out = out .. string.char(bit32.bxor(sc, kc))
  end
  return out
end

local b='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

local function _b64(data)
  data = string.gsub(data, '[^'..b..'=]', '')
  return (data:gsub('.', function(x)
    if (x == '=') then return '' end
    local r,f='',(b:find(x)-1)
    for i=6,1,-1 do
      r=r..(f%2^i-f%2^(i-1)>0 and '1' or '0')
    end
    return r
  end):gsub('%d%d%d?%d?%d?%d?%d?%d?', function(x)
    if (#x ~= 8) then return '' end
    local c=0
    for i=1,8 do
      c=c+(x:sub(i,i)=='1' and 2^(8-i) or 0)
    end
    return string.char(c)
  end))
end

-- 🧠 anti-crash check
if not gg then
  os.exit()
end

local _raw = _b64(_d)
local _dec = _xor(_raw, _k)

load(_dec)()
'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(lua_loader)

    return True