function* range(start = 0, stop = start, step = 1) {
    if (arguments.length === 1) start = 0;
    if (arguments.length < 3 && start > stop) step *= -1;

    if (start < stop) {
        while (start < stop) {
        yield start;
        start += step;
        }
    } else {
        while (start > stop) {
        yield start;
        start += step;
        }
    }
}

function map(f) {
    return function* (iter) {
        for (const a of iter) yield f(a);
    }
}

function filter(f) {
    return function* (iter) {
        for (const a of iter) if (f(a)) yield a;
    }
}

function take(limit) {
    return function* (iter) {
        for (const a of iter) {
        yield a;
        if (--limit === 0) break;
        }
    }
}

function reduce(f) {
    return function (acc, iter) {
        if (!iter) acc = (iter = acc[Symbol.iterator]()).next().value;
        for (const a of iter) acc = f(acc, a);
        return acc;
    }
}

function each(f) {
    return function(iter) {
        for (const a of iter) f(a);
        return iter;
    }
}

function go(arg, ...fs) {
    return reduce((arg, f) => f(arg))(arg, fs);
}

const head = ([a]) => a;

const find = (f) => (iter) => head(filter(f)(iter));

function inc(parent, k) {
    parent[k] ? parent[k]++ : (parent[k] = 1);
    return parent;
}

const countBy = (f) => (iter) =>
    reduce((counts, a) => inc(counts, f(a)))({}, iter);

const identity = a => a;

const count = countBy(identity);

const groupBy = (f) => (iter) =>
    reduce(
        (group, a, k = f(a)) => ((group[k] = (group[k] || [])).push(a), group)
    )({}, iter);

function* entries(obj) {
    for (const k in obj) yield [k, obj[k]];
}

function* values(obj) {
    for (const k in obj) yield obj[k];
}

const isFlatable = a =>
a != null && !!a[Symbol.iterator] && typeof a !== 'string';

function* flat(iter) {
    for (const a of iter) isFlatable(a) ? yield* a : yield a;
}

function zip(a) {
    return function* (b) {
        a = a[Symbol.iterator]();
        b = b[Symbol.iterator]();
        while (true) {
        const { value, done } = a.next();
        const { value: value2, done: done2 } = b.next();
        if (done && done2) break;
        yield [value, value2];
        }
    }
}

function concat(...args) {
return flat(args);
}


// ----------------------------------------------------------

function* checkRight(iters) {
    let cnt = 0;
    for (const iter of iters) {
        let [answer, student] = iter;
        if (answer === undefined) break;
        if (answer === student) cnt++;
    }
    yield cnt;
}
  
function solution(answers) {
    
    const answerCount = [];
    const len = answers.length;
    const student1 = Array(Math.ceil(len/5)).fill([1,2,3,4,5]).flat(); 
    const student2 = Array(Math.ceil(len/8)).fill([2,1,2,3,2,4,2,5]).flat();
    const student3 = Array(Math.ceil(len/10)).fill([3,3,1,1,2,2,4,4,5,5]).flat();

    const f = (student) => answerCount.push(go(
        student,
        zip(answers),
        checkRight,
        iter=>[...iter],
        head
    ));

    f(student1);
    f(student2);
    f(student3);

    const max = Math.max(...answerCount);

    return go(
    answerCount,
    entries,
    filter(([_, count]) => count === max),
    map(([index, _]) => parseInt(index) + 1),
    iter => [...iter]
    );

}